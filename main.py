import os
import requests
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient

AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
SERVICE_PRINCIPAL_AZURE_APP_ID = os.environ['SERVICE_PRINCIPAL_AZURE_APP_ID']
SERVICE_PRINCIPAL_AZURE_APP_SECRET = os.environ['SERVICE_PRINCIPAL_AZURE_APP_SECRET']
AZURE_KEY_VAULT_URL = os.environ['AZURE_KEY_VAULT_URL']
AZURE_KEY_VAULT_API_NAME_NASA_GOV = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']
AZURE_STORAGE_ACCOUNT_URL = os.environ['AZURE_STORAGE_ACCOUNT_URL']

credential = ClientSecretCredential(
    tenant_id=AZURE_TENANT_ID,
    client_id=SERVICE_PRINCIPAL_AZURE_APP_ID,
    client_secret=SERVICE_PRINCIPAL_AZURE_APP_SECRET
)

secret_client = SecretClient(vault_url=AZURE_KEY_VAULT_URL, credential=credential)
secret = secret_client.get_secret(AZURE_KEY_VAULT_API_NAME_NASA_GOV)

NASA_API_KEY = secret.value

def retrieve_data_from_nasa_api(api_key, start_date, end_date):
    url = f"https://api.nasa.gov/DONKI/CME?startDate={start_date}&endDate={end_date}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

#sample_data = retrieve_data_from_nasa_api(NASA_API_KEY, "2023-06-23", "2023-07-23")

# connect to azure storage

from azure.storage.blob import ContainerClient

service = BlobServiceClient(account_url=AZURE_STORAGE_ACCOUNT_URL, credential=credential)

print(next(service.list_containers()))





