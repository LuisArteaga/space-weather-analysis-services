import os
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient


AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
SERVICE_PRINCIPAL_AZURE_APP_ID = os.environ['SERVICE_PRINCIPAL_AZURE_APP_ID']
SERVICE_PRINCIPAL_AZURE_APP_SECRET = os.environ['SERVICE_PRINCIPAL_AZURE_APP_SECRET']
AZURE_KEY_VAULT_URL = os.environ['AZURE_KEY_VAULT_URL']
AZURE_STORAGE_ACCOUNT_URL = os.environ['AZURE_STORAGE_ACCOUNT_URL']

class AzureServicesConnector():
    def __init__(self):
        self.credential = ClientSecretCredential(
            tenant_id=AZURE_TENANT_ID,
            client_id=SERVICE_PRINCIPAL_AZURE_APP_ID,
            client_secret=SERVICE_PRINCIPAL_AZURE_APP_SECRET
        )
        self.key_vault_client = SecretClient(
            vault_url=AZURE_KEY_VAULT_URL,
            credential=self.credential
        )
        self.blob_service_client = BlobServiceClient(
            account_url=AZURE_STORAGE_ACCOUNT_URL,
            credential=self.credential
        )

    def get_secret(self, secret_name):
        return self.key_vault_client.get_secret(secret_name).value

    def get_container_client(self, container_name):
        return self.blob_service_client.get_container_client(container_name)
