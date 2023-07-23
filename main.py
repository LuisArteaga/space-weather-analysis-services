import os
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential

AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
SERVICE_PRINCIPAL_AZURE_APP_ID = os.environ['SERVICE_PRINCIPAL_AZURE_APP_ID']
SERVICE_PRINCIPAL_AZURE_APP_SECRET = os.environ['SERVICE_PRINCIPAL_AZURE_APP_SECRET']
AZURE_KEY_VAULT_URL = os.environ['AZURE_KEY_VAULT_URL']
AZURE_KEY_VAULT_API_NAME_NASA_GOV = os.environ['AZURE_KEY_VAULT_API_NAME_NASA_GOV']

credential = ClientSecretCredential(
    tenant_id=AZURE_TENANT_ID,
    client_id=SERVICE_PRINCIPAL_AZURE_APP_ID,
    client_secret=SERVICE_PRINCIPAL_AZURE_APP_SECRET
)

secret_client = SecretClient(vault_url=AZURE_KEY_VAULT_URL, credential=credential)
secret = secret_client.get_secret(AZURE_KEY_VAULT_API_NAME_NASA_GOV)
print(secret.value)

