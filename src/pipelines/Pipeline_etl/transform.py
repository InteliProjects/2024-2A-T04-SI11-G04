import dask.dataframe as dd
from Utils.transform_utils import optimize_floats
import pandas as pd 

class Transform:
    def __init__(self, consumption_data: dd.DataFrame, fraud_data: dd.DataFrame):
        self.consumption_data = consumption_data
        self.fraud_data = fraud_data
    def create_anomes(self) -> None:
        self.consumption_data = self.consumption_data.assign(
            REFERENCIA=dd.to_datetime(self.consumption_data['REFERENCIA'], format='%Y-%m-%d', errors='coerce')
        )
        self.consumption_data = self.consumption_data.assign(
            ANOMES=self.consumption_data['REFERENCIA'].apply(lambda x: f"{x.month:02}/{str(x.year)[-2:]}" if pd.notnull(x) else None, meta=('ANOMES', 'object'))
        )
        print(self.consumption_data[['REFERENCIA', 'ANOMES']].head()) # Verificação
        
    def reduce_columns(self) -> None:
        cols_to_drop = [
            'EMP_CODIGO', 'COD_GRUPO', 'COD_SETOR_COMERCIAL', 'NUM_QUADRA',
            'COD_ROTA_LEITURA', 'ECO_RESIDENCIAL', 'ECO_COMERCIAL', 'ECO_INDUSTRIAL',
            'ECO_PUBLICA', 'ECO_OUTRAS', 'LTR_ATUAL', 'LTR_COLETADA', 'DAT_LEITURA',
            'DSC_OCORRENCIA', 'COD_LEITURA_INF_1', 'COD_LEITURA_INF_2',
            'COD_LEITURA_INF_3', 'HORA_LEITURA', 'DSC_SIMULTANEA',
            'COD_LEITURA_INT', 'STA_TROCA', 'STA_ACEITA_LEITURA'
        ]

        self.consumption_data = self.consumption_data.drop(columns=cols_to_drop)
        self.fraud_data = self.fraud_data[['MATRICULA', 'ANOMES', 'ANOOS']]
        
    def transform_datatypes(self) -> None:
        self.consumption_data = self.consumption_data.assign(
            MATRICULA=self.consumption_data['MATRICULA']
            .astype(str)
            .str.replace('.', '', regex=False)
            .str.rstrip('0')
        )
        self.fraud_data = self.fraud_data.assign(
            MATRICULA=self.fraud_data['MATRICULA'].astype(str)
            .str.replace('.', '', regex=False)
            .str.rstrip('0'),
            ANOOS=self.fraud_data['ANOOS']
            .astype(str)  # Converte para string
            .str.replace('.0', '', regex=False)  
        )

        print(self.fraud_data[['ANOOS']].head())  # Verificação após o processamento
        
    def set_index(self) -> None:
        # Remover NaNs nas colunas de índice
        self.consumption_data = self.consumption_data.dropna(subset=['REFERENCIA'])
        self.fraud_data = self.fraud_data.dropna(subset=['ANOOS'])
        self.fraud_data = self.fraud_data[self.fraud_data['ANOOS'] > '2018']
        # Calcular anos únicos para consumption_data e fraud_data
        consumption_divisions = self.consumption_data['REFERENCIA'].dt.year.unique().compute().tolist()
        fraud_divisions = self.fraud_data['ANOOS'].astype(int).unique().compute().tolist()

        # Alinhar as divisões
        aligned_divisions = sorted(set(consumption_divisions).union(fraud_divisions))

        # Definir o índice e reordenar conforme as divisões alinhadas
        self.consumption_data = self.consumption_data.assign(
            ANO=self.consumption_data['REFERENCIA'].dt.year
        ).set_index('ANO', sorted=True).repartition(divisions=aligned_divisions)

        self.fraud_data = self.fraud_data.assign(
            ANO=self.fraud_data['ANOOS'].astype(int)
        ).set_index('ANO', sorted=True).repartition(divisions=aligned_divisions)

        # Verificar particionamento
        self._check_partitioning(self.consumption_data, 'consumption_data')
        self._check_partitioning(self.fraud_data, 'fraud_data')


    def left_join_fraudes(self) -> dd.DataFrame:
        # Alinhar tipos de dados
        # Garantir que ambas as colunas ANOMES sejam do tipo string
        self.consumption_data['ANOMES'] = self.consumption_data['ANOMES'].astype(str)
        self.fraud_data['ANOMES'] = self.fraud_data['ANOMES'].astype(str)
        print(self.fraud_data[['ANOMES']].head())  # Verificação após o processamento
        print(self.consumption_data[['ANOMES']].head())  # Verificação após o processamento
        print(self.consumption_data['ANOMES'].dtype)
        print(self.fraud_data['MATRICULA'].head())
        # Realizar a junção
        merged_data = dd.merge(
            self.consumption_data, 
            self.fraud_data, 
            on=['ANOMES', 'MATRICULA'], 
            how='left', 
            indicator=True
        )
    
        merged_data = merged_data.assign(
            FRAUDE=(merged_data['_merge'] == 'both').astype('int32')
        ).drop(columns=['_merge', 'Unnamed: 0'])
        
        print(merged_data['FRAUDE'].sum().compute())

        return merged_data


    
    def _check_partitioning(self, df: dd.DataFrame, df_name: str) -> None:
        """Verifica e imprime informações sobre o particionamento do DataFrame."""

        print(f"\nVerificando particionamento de {df_name}:")
        print(f"Número de partições: {df.npartitions}")
        print(f"Divisões conhecidas: {df.known_divisions}")
        
        if df.known_divisions:
            print(f"Amostra das divisões: {df.divisions[:5]} ... {df.divisions[-5:]}")  # Imprime algumas divisões
        else:
            print("As divisões não são conhecidas, o que pode indicar que o DataFrame não está particionado de forma otimizada.")

class TransformerExternal:
    def __init__(self, df_weather, df_days, df_shows, df_bcb):
        self.df_weather = df_weather
        self.df_days = df_days
        self.df_shows = df_shows
        self.df_bcb = df_bcb

    def merge_weather_days(self, df_weather, df_days):
        # Ensure 'REFERENCIA' is in the correct format in both dataframes
        df_weather['REFERENCIA'] = pd.to_datetime(df_weather.index)
        df_days['REFERENCIA'] = pd.to_datetime(df_days['REFERENCIA'])
        return df_weather.merge(df_days, on='REFERENCIA', how='left')

    def dummy_days(self, df):  # Adicionado 'self'
        return pd.get_dummies(df, columns=['tipo_dia'])

    def create_anomes(self, df):  # Adicionado 'self'
        df['ANOMES'] = df['REFERENCIA'].dt.strftime('%m/%y')
        return df

    def groupby_df_weather_days(self, df):  # Adicionado 'self'
        return df.groupby(['ANOMES']).agg({
            'Temperature (°C)': 'mean',
            'Precipitation (mm)': 'sum',
            'Wind Speed (km/h)': 'mean',
            'Wind Direction (°)': 'mean',
            'tipo_dia_dia_util': 'sum',
            'tipo_dia_fim_de_semana': 'sum',
            'tipo_dia_feriado': 'sum'
        }).reset_index()

    def groupby_df_shows(self, df):  # Adicionado 'self'
        # Usar função anomes
        def convert_date(x):
            if pd.isna(x):
                return x
            # Converter para string no formato 'MM/AAAA'
            x_str = x.strftime('%m/%Y')
            # Aplicar slicing para obter o formato 'MM/AA'
            return x_str[:3] + x_str[-2:]
        df['ANOMES'] = df['REFERENCIA'].apply(convert_date)
        return df.groupby('ANOMES').size().reset_index(name='quantidade_shows')

    def merge_all_df_byAnomes(self, df_weather_days, df_shows, df_bcb):  # Adicionado 'self'
        return df_weather_days.merge(df_shows, on='ANOMES', how='left').merge(df_bcb, on='ANOMES', how='left')

    def run_transform(self):
        # Ensure df_weather has a 'REFERENCIA' column
        self.df_weather['REFERENCIA'] = self.df_weather.index
        
        df_weather_days = self.merge_weather_days(self.df_weather, self.df_days)
        df_weather_days = self.dummy_days(df_weather_days)
    
        df_weather_days = self.create_anomes(df_weather_days)
        df_weather_days = self.groupby_df_weather_days(df_weather_days)
        
        df_shows = self.groupby_df_shows(self.df_shows)
        
        df_final = self.merge_all_df_byAnomes(df_weather_days, df_shows, self.df_bcb)
        
        return df_final

    
        
        
    

