import os
import dask.dataframe as dd
from extract import Extract, BcbExtractor, WeatherDataExtractor, DayTypeIdentifier, ShowExtractor
from transform import Transform, TransformerExternal
from dask.distributed import Client
from dask.diagnostics import ProgressBar

class Pipeline:
    def __init__(self, config):
        self.config = config

    def run(self):
        # Convert anos to integers
        anos = [int(year) for year in self.config['anos']]
        
        # Step 1: Extract Data
        extract = Extract(self.config['dircsv'], self.config['fraudfile'], anos, self.config['sep'])
        extract.extract_csv_files()
        extract.extract_frauds()
        consumption_data = extract.get_dataframes()
        fraud_data = extract.get_frauds()

        # Extracting additional external data
        bcb_extractor = BcbExtractor(self.config['api_list'], self.config['endpoint_names'], self.config['params'])
        bcb_extractor.extract_bcb()
        bcb_data = bcb_extractor.get_bcb()

        weather_extractor = WeatherDataExtractor(self.config['start'], self.config['end'], self.config['country'], self.config['state'], self.config['city'])
        weather_data = weather_extractor.fetch_data()

        day_identifier = DayTypeIdentifier(self.config['state'], self.config['start_year'], self.config['end_year'])
        day_data = day_identifier.criar_coluna_referencia(self.config['start_date'], self.config['end_date'])

        show_extractor = ShowExtractor(self.config['base_url'], self.config['country_show'], self.config['query'])
        show_extractor.extract_all_shows()
        show_data = show_extractor.to_dataframe()

        # Step 2: Transform Data
        transform = Transform(consumption_data, fraud_data)
        transform.create_anomes()
        transform.reduce_columns()
        transform.transform_datatypes()
        transform.set_index()
        merged_data = transform.left_join_fraudes()

        transformer_external = TransformerExternal(weather_data, day_data, show_data, bcb_data)
        final_data = transformer_external.run_transform()
        # Drop duplicates in external data
        final_data = final_data.drop_duplicates()

        # Step 3: Partition and Save Data Separately
        # Create separate directories for consumption and external data
        consumption_output_dir = os.path.join(self.config['output_dir'], 'consumption')
        external_output_dir = os.path.join(self.config['output_dir'], 'external')
        os.makedirs(consumption_output_dir, exist_ok=True)
        os.makedirs(external_output_dir, exist_ok=True)

        consumption_parquet_path = os.path.join(consumption_output_dir, 'consumption_data.parquet')
        external_parquet_path = os.path.join(external_output_dir, 'external_data.parquet')

        # Use ProgressBar to monitor the task
        with ProgressBar():
            merged_data.to_parquet(consumption_parquet_path, engine='pyarrow')
            print("Saving consumption data...")
            final_data.to_parquet(external_parquet_path, engine='pyarrow')
            print("Saving external data...")

        # Step 4: Merge Data (Using Dask to handle large datasets)
        final_merged_data = dd.merge(merged_data, final_data, on='ANOMES', how='left')
        # Save the final merged dataset
        final_output_parquet_path = os.path.join(self.config['output_dir'], 'final_dataset.parquet')

        with ProgressBar():
            final_merged_data.to_parquet(final_output_parquet_path, engine='pyarrow')

        print(f"Consumption data saved to {consumption_parquet_path}")
        print(f"External data saved to {external_parquet_path}")
        print(f"Final merged data saved to {final_output_parquet_path}")

    def __del__(self):
        # Ensure the client is closed when the Pipeline object is destroyed
        if hasattr(self, 'client'):
            self.client.close()

if __name__ == "__main__":
    # Configuration based on your provided parameters
    config = {
        'dircsv': 'G:/Shared drives/AEGEA/DADOS',
        'fraudfile': 'FRAUDES_HIST',
        'anos': [2021, 2022, 2023, 2024],  # List of years
        'sep': ';',
        'api_list': {
            'IGPM': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados?formato=json',
            'SELIC': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json',
            'IPCA': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
        },
        'endpoint_names': ['IGPM', 'SELIC', 'IPCA'],
        'params': {
            'dataInicial': '01/01/2021',
            'dataFinal': '10/08/2024'
        },
        'start': '2021-01-01',
        'end': '2024-08-10',
        'country': 'BR',
        'state': 'MS',
        'city': 'Campo Grande',
        'start_year': 2021,
        'end_year': 2024,
        'start_date': '2021-01-01',
        'end_date': '2024-08-10',
        'country_show': 'br',
        'base_url': 'https://www.setlist.fm/search',
        'query': 'Campo+Grande',
        'output_dir': 'G:/Shared drives/AEGEA/DADOS/output',
    }

    pipeline = Pipeline(config)
    pipeline.run()
