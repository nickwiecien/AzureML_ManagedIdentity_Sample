from azure.identity import ManagedIdentityCredential, DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


#System-Assigned Identity
credential = ManagedIdentityCredential()

#User-Assigned Identity - Needs Client ID
# credential = ManagedIdentityCredential(client_id='<YOUR-MI-CLIENT-ID>')

client = SecretClient(vault_url=f"<YOUR-KEY-VAULT-URI>", credential=credential)
value = client.get_secret('<YOUR-SECRET-NAME>')
print(value.value)
