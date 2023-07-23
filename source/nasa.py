import os
import requests

class NasaGovAPI():

    def __init__(self):
        self.key_vault_api_name_nasa_gov = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']
        self.azure_storage_container_name = os.environ['AZURE_STORAGE_CONTAINER_NAME']

    def get_key_vault_api_name_nasa_gov(self):
        return self.key_vault_api_name_nasa_gov
        
    def extract_coronal_mass_ejection(self, start_date, end_date):
        url = f"https://api.nasa.gov/DONKI/CME?startDate={start_date}&endDate={end_date}&api_key={self.key_vault_api_name_nasa_gov}"
        response = requests.get(url)
        data = response
        return data
