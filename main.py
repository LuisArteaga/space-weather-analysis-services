import config
import utils
from source.nasa import NasaGovAPI

AzureServicesConnector = config.AzureServicesConnector()
NasaGovAPI = NasaGovAPI()

nasa_api_key = AzureServicesConnector.get_secret(NasaGovAPI.get_key_vault_api_name_nasa_gov())
storage_container = AzureServicesConnector.get_container_client()

extraction_start_date, extraction_end_date = utils.get_param_to_date_time_frame(7)

extract_cme_status = NasaGovAPI.extract_data_from_nasa_api(start_date=extraction_start_date, end_date=extraction_end_date, storage_container=storage_container, api_key=nasa_api_key, api_name='coronal-mass-ejection')


extract_flr_status = NasaGovAPI.extract_data_from_nasa_api(start_date=extraction_start_date, end_date=extraction_end_date, storage_container=storage_container, api_key=nasa_api_key, api_name='solar-flare')


extract_gst_status = NasaGovAPI.extract_data_from_nasa_api(start_date=extraction_start_date, end_date=extraction_end_date, storage_container=storage_container, api_key=nasa_api_key, api_name='geomagnetic-storm')
