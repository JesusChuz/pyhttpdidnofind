import os
import azure.functions as func
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Check if deployed to Azure
   # if 'WEBSITE_SITE_NAME' in os.environ:
        # Using Managed Identity when deployed to Azure
    managed_identity_client_id="bb396450-be68-4036-8d4c-f11d70690060"
    credential = ManagedIdentityCredential(client_id=managed_identity_client_id)
    #else:
        # Using DefaultAzureCredential for local development
     #   credential = DefaultAzureCredential()

    # Create SecretClient with appropriate credential
    secret_client = SecretClient(vault_url="https://jesumekvpymsi.vault.azure.net/", credential=credential)
    secret_name = "mysecret"
    secret_value = secret_client.get_secret(secret_name).value
 

    identityendpoint = os.environ.get('IDENTITY_ENDPOINT')
    identitysecret = os.environ.get('IDENTITY_SECRET')


    return func.HttpResponse(f"The secret value is: {secret_value}, endpoint: {identityendpoint} , secret: {identitysecret}")
