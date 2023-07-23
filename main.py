import config
from source.nasa import NasaGovAPI

AzureServicesConnector = config.AzureServicesConnector()
NasaGovAPI = NasaGovAPI()

nasa_api_key = AzureServicesConnector.get_secret(NasaGovAPI.get_key_vault_api_name_nasa_gov())
storage_container = AzureServicesConnector.get_container_client()

extraction_start_date = "2023-06-23"
extraction_end_date = "2023-07-23"

extract_cme_status = NasaGovAPI.extract_coronal_mass_ejection(start_date=extraction_start_date, end_date=extraction_end_date, storage_container=storage_container)

print(extract_cme_status)

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




