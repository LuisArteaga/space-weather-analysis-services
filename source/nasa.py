import os
import datetime
import requests

class NasaGovAPI():

    def __init__(self):
        self.key_vault_api_name_nasa_gov = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']
        self.azure_storage_container_name = os.environ['AZURE_STORAGE_CONTAINER_NAME']

    def get_key_vault_api_name_nasa_gov(self):
        return self.key_vault_api_name_nasa_gov
        
    def extract_coronal_mass_ejection(self, start_date, end_date, storage_container):
        url = f"https://api.nasa.gov/DONKI/CME?startDate={start_date}&endDate={end_date}&api_key={self.key_vault_api_name_nasa_gov}"
        start_date_stripped = start_date.replace("-", "")
        end_date_stripped = end_date.replace("-", "") 
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"nasa-gov/donki/coronal-mass-ejection/01-raw/coronal_mass_ejection__refdate_{start_date_stripped}_to_{end_date_stripped}__created_on_{timestamp}.json"
        response = requests.get(url, timeout=30)
        data = response
        storage_container.upload_blob(name=file_name, data=data)
        
        #ToDO: get attribute/function to display code 200 for ok etc.
        return requests.Response()