import config
import utils
from source.nasa import NasaGovAPI

AzureServicesConnector = config.AzureServicesConnector()
NasaGovAPI = NasaGovAPI()

nasa_api_key = AzureServicesConnector.get_secret(NasaGovAPI.get_key_vault_api_name_nasa_gov())
storage_container = AzureServicesConnector.get_container_client()

extraction_start_date, extraction_end_date = utils.get_param_to_date_time_frame(7)

extract_cme_status = NasaGovAPI.extract_coronal_mass_ejection(start_date=extraction_start_date, end_date=extraction_end_date, storage_container=storage_container)

