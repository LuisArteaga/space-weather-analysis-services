import os
import datetime
import requests

class NasaGovAPI():

    def __init__(self):
        self.key_vault_api_name_nasa_gov = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']
        self.azure_storage_container_name = os.environ['AZURE_STORAGE_CONTAINER_NAME']
        self.api_list = {'coronal-mass-ejection': 'https://api.nasa.gov/DONKI/CME',
                         'geomagnetic-storm' : 'https://api.nasa.gov/DONKI/GST',
                         'solar-flare': 'https://api.nasa.gov/DONKI/FLR',
                         'solar-energetic-particle': 'https://api.nasa.gov/DONKI/SEP',
                         'magnetopause-crossing': 'https://api.nasa.gov/DONKI/MPC',
                         'radiation-belt-enhancement': 'https://api.nasa.gov/DONKI/RBE','hight-speed-stream': 'https://api.nasa.gov/DONKI/HSS',
                         'WSA-Enlil-Simulation': 'https://api.nasa.gov/DONKI/WSAEnlilSimulations',
                         'notifications': 'https://api.nasa.gov/DONKI/notifications'}
    
    def get_key_vault_api_name_nasa_gov(self):
        return self.key_vault_api_name_nasa_gov
    
    def _create_file_name(self, start_date, end_date, api_name):
        start_date_stripped = start_date.replace("-", "")
        end_date_stripped = end_date.replace("-", "")
        folder_name = f"nasa-gov/donki/{api_name}/01-raw/"
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        
        file_name = f"{folder_name}{api_name}-refdate-from-{start_date_stripped}-to-{end_date_stripped}-created-on-{timestamp}.json"
        
        return file_name
    
    def extract_data_from_nasa_api(self, start_date, end_date, storage_container, api_key, api_name):
        
        api_base_url = self.api_list[api_name]
        
        url = f"{api_base_url}?startDate={start_date}&endDate={end_date}&api_key={api_key}"

        file_name = self._create_file_name(start_date=start_date, end_date=end_date, api_name=api_name)
        response = requests.get(url, timeout=30)
        data = response
        storage_container.upload_blob(name=file_name, data=data)
        
        #ToDO: get attribute/function to display code 200 for ok etc.
        return requests.Response()