import os
import requests
import config

AzureServicesConnector = config.AzureServicesConnector()

AZURE_KEY_VAULT_API_NAME_NASA_GOV = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']
AZURE_STORAGE_CONTAINER_NAME = os.environ['AZURE_STORAGE_CONTAINER_NAME']

nasa_api_key = AzureServicesConnector.get_secret(AZURE_KEY_VAULT_API_NAME_NASA_GOV)
storage_container = AzureServicesConnector.get_container_client(AZURE_STORAGE_CONTAINER_NAME)

def retrieve_data_from_nasa_api(api_key, start_date, end_date):
    url = f"https://api.nasa.gov/DONKI/CME?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    response = requests.get(url)
    data = response
    return data

sample_data = retrieve_data_from_nasa_api(nasa_api_key, "2023-06-23", "2023-07-23")

storage_container.upload_blob(name="nasa-gov/donki/coronal-mass-ejection/01-raw/sample_data.json", data=sample_data)




#print(next(service.list_containers()))

# Save sample_data in blob nasa-gov
#container.upload_blob(name="sample_data.json", data=sample_data)
#print(container.get_blob_client("sample_data.json").url)
# print(container.get_blob_client("sample_data.json").download_blob().readall())
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.content_type)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.content_encoding)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.content_language)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.cache_control)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.content_disposition)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.content_md5)
# print(container.get_blob_client("sample_data.json").download_blob().content_settings.last_modified)
# print(container.get_blob_client("sample_data.json").download_blob().metadata)




