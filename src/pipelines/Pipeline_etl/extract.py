import dask.dataframe as dd
import os
import requests
import pandas as pd
from functools import reduce
import json
import numpy as np
from meteostat import Stations, Daily
from datetime import datetime
import holidays
from bs4 import BeautifulSoup
class Extract:
    def __init__(self, dircsv, fraudfile, anos, sep):
        self.dircsv = dircsv
        self.fraudfile = fraudfile
        self.anos = anos
        self.dataframes = None
        self.frauds = None
        self.sep = sep
        
    def extract_csv_files(self):
        dtype = {
            'FATURADO_MEDIA': 'object',
            'DESCRSETORSOLICITANTE': 'object',
            'MOTIVOEXECOCOR': 'object',
            'NR_ROTA': 'object',
            'SF': 'object'
        }
        
        file_pattern = os.path.join(self.dircsv, 'CONSUMO_*', 'CONSUMO_*.csv')
        
        self.dataframes = dd.read_csv(file_pattern, sep=self.sep, assume_missing=True, dtype=dtype)
        
        # Filter for specified years
        self.dataframes['REFERENCIA'] = dd.to_datetime(self.dataframes['REFERENCIA'])
        self.dataframes = self.dataframes[self.dataframes['REFERENCIA'].dt.year.isin(self.anos)]
            
    def extract_frauds(self):
        dtype = {
            'DESCRSETORSOLICITANTE': 'object',
            'MOTIVOEXECOCOR': 'object',
            'NR_ROTA': 'object',
            'SF': 'object'
        }
        
        filepath = os.path.join(self.dircsv, f'{self.fraudfile}/{self.fraudfile}.csv')
        self.frauds = dd.read_csv(filepath, sep=self.sep, assume_missing=True, dtype=dtype)
        
        # Filter for specified years
        self.frauds['ANOOS'] = self.frauds['ANOOS'].astype(int)
        self.frauds = self.frauds[self.frauds['ANOOS'].isin(self.anos)]
    def get_dataframes(self):
        return self.dataframes
    
    def get_frauds(self):
        return self.frauds
    
class BcbExtractor:
    def __init__(self, api_list, endpoint_names, params, end_data=None):
        self.api_list = api_list
        self.endpoint_names = endpoint_names
        self.params = params
        self.end_data = end_data
        self.data_list = []
        self.dataframe = None
    
    def extract_bcb(self):
        for i in self.endpoint_names:
            try:
                url = self.api_list.get(i)
                if not url:
                    print(f"URL não encontrada para o endpoint: {i}")
                    continue

                response = requests.get(url, params=self.params)
                if response.status_code == 200:
                    print(f"Resposta de {url}: {response.text[:500]}")  # Imprime os primeiros 500 caracteres da resposta
                    try:
                        data = response.json()
                        if not data:
                            print(f"Nenhum dado retornado para o endpoint: {i}")
                            continue
                        
                        data = pd.DataFrame(data)
                        if data.empty:
                            print(f"DataFrame vazio para o endpoint: {i}")
                            continue
                        
                        data['data'] = pd.to_datetime(data['data'], format="%d/%m/%Y", errors="coerce")
                        data['ano'] = data['data'].dt.year
                        data['valor_' + i] = pd.to_numeric(data['valor'], errors='coerce')
                        data['ANOMES'] = data['data'].dt.strftime('%m/%y')
                        data = data.drop(columns=['data', 'valor'])
                        
                        print(f"DataFrame para o endpoint {i}:")
                        print(data.head())  # Imprime as primeiras linhas do DataFrame para verificação
                        
                        self.data_list.append(data)
                    except ValueError as e:
                        print(f"Erro ao processar JSON para o endpoint {i}: {e}")
                else:
                    print(f"Falha ao obter dados de {url}: Código de status {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Erro na requisição para o endpoint {i}: {e}")

        if self.data_list:
        # Inicia com o primeiro DataFrame da lista
            merged_data = self.data_list[0]
            
            # Realiza o merge com base na coluna 'ANOMES' para os DataFrames subsequentes
            for df in self.data_list[1:]:
                merged_data = pd.merge(merged_data, df, on='ANOMES', how='outer')
            
            self.dataframe = merged_data
            print(f"DataFrame merged com sucesso. Shape: {self.dataframe.shape}")
        else:
            print("Nenhum dado foi extraído.")
    
    def get_bcb(self):
        self.dataframe.drop(columns=['ano_x', 'ano_y'], inplace=True)
        return self.dataframe
class WeatherDataExtractor:
    def __init__(self, start, end, country, state, city):
        self.start = start
        self.end = end
        self.country = country
        self.state = state
        self.city = city
        self.station = self._get_station()
    
    def _get_station(self):
        # Busca a estação meteorológica específica com base na cidade, estado e país
        stations = Stations()
        stations = stations.region(self.country, self.state).fetch()
        station = stations[stations['name'] == self.city].iloc[0]
        return station
    
    def fetch_data(self):
        # Obter o código WMO da estação
        wmo_code = self.station['wmo']
        
        # Buscar dados diários da estação para o período especificado
        data = Daily(wmo_code, self.start, self.end).fetch()
        
        # Definir as colunas de interesse
        selected_columns = ['tavg', 'prcp', 'rhum', 'wspd', 'wdir', 'srad']
        available_columns = [col for col in selected_columns if col in data.columns]
        
        # Filtrar apenas as colunas disponíveis
        data = data[available_columns]
        
        # Renomear colunas para uma nomenclatura mais legível
        column_names = {
            'tavg': 'Temperature (°C)',
            'prcp': 'Precipitation (mm)',
            'rhum': 'Relative Humidity (%)',
            'wspd': 'Wind Speed (km/h)',
            'wdir': 'Wind Direction (°)',
            'srad': 'Solar Radiation (W/m²)'
        }
        
        data.rename(columns=column_names, inplace=True)
        return data

class DayTypeIdentifier:
    def __init__(self, state, start_year, end_year):
        # Inicializar os feriados do Brasil para o estado específico
        self.feriados = holidays.Brazil(state=state, years=range(start_year, end_year + 1))
    
    def _identificar_tipo_dia(self, data):
        # Função auxiliar para classificar o tipo de dia
        if data in self.feriados:
            return 'feriado'
        elif data.weekday() >= 5:  # Sábado (5) ou Domingo (6)
            return 'fim_de_semana'
        else:
            return 'dia_util'
    
    def aplicar_tipo_dia(self, df):
        # Criar a coluna REFERENCIA e aplicar a função de identificar tipo de dia
        df['tipo_dia'] = df['REFERENCIA'].apply(self._identificar_tipo_dia)
        return df

    def criar_coluna_referencia(self, start_date, end_date):
        # Criar um DataFrame com a coluna REFERENCIA no formato YYYY-MM-DD
        df = pd.DataFrame({
            'REFERENCIA': pd.date_range(start=start_date, end=end_date, freq='D')
        })
        # Aplicar a função para identificar tipo de dia
        df = self.aplicar_tipo_dia(df)
        return df

    
class ShowExtractor:
    def __init__(self, base_url, country, query):
        self.base_url = base_url
        self.country = country
        self.query = query
        self.all_data = []

    def extract_shows_from_page(self, page_number):
        # Atualizar o link para incluir o número da página
        link = f'{self.base_url}?page={page_number}&country={self.country}&query={self.query}'
        
        # Fazer a requisição
        response = requests.get(link)
        
        # Criar o objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todos os blocos que contêm as informações dos shows
        shows = soup.find_all('div', class_='col-xs-12 setlistPreview')
        
        # Lista para armazenar os dados da página
        data = []
        
        # Iterar sobre todos os shows e extrair as datas e o artista
        for show in shows:
            # Extrair a data (mês, dia e ano)
            month = show.find('span', class_='month').text
            day = show.find('span', class_='day').text
            year = show.find('span', class_='year').text
            date = f"{month} {day}, {year}"
            
            # Extrair o artista
            details = show.find_next('div', class_='details')
            artist = details.find('span').find('span').text
            
            # Adicionar as informações à lista
            data.append({'REFERENCIA': date, 'Artist': artist})
        
        return data

    def extract_all_shows(self, total_pages=13):
        # Iterar sobre as páginas para extrair os shows
        for page in range(1, total_pages + 1):
            page_data = self.extract_shows_from_page(page)
            self.all_data.extend(page_data)

    def to_dataframe(self):
        # Converter os dados para DataFrame e ajustar a coluna de data
        data_df = pd.DataFrame(self.all_data)
        data_df['REFERENCIA'] = pd.to_datetime(data_df['REFERENCIA'])
        return data_df
    
        
                        
                    
                    
                        
                    
        
        
