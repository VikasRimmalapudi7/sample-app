import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault name
KEY_VAULT_NAME = 'pythonsampleapp-cert'
# Replace with your secret name
SECRET_NAME = 'sample-secret'

# Construct the Key Vault URL
key_vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net/"

# Create a credential using Azure Identity
credential = DefaultAzureCredential()

# Create a SecretClient to interact with the Key Vault
client = SecretClient(vault_url=key_vault_url, credential=credential)

try:
    # Retrieve the secret
    secret = client.get_secret(SECRET_NAME)
    
    # Print the secret value (assumed to be JSON)
    json_data = json.loads(secret.value)
    
    # Print each key-value pair line by line
    print("Retrieved JSON secret:")
    for key, value in json_data.items():
        print(f"{key}: {value}")  # Print each key-value pair

except Exception as e:
    print(f"An error occurred: {e}")