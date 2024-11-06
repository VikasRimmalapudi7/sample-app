from flask import Flask, jsonify
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
import json

app = Flask(__name__)

KEY_VAULT_NAME = 'pythonsampleapp-cert'
SECRET_NAME = 'sample-secret'
key_vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net/"
credential = ManagedIdentityCredential(client_id="c318642b-0415-490d-b0a4-1bdc3c6bda27")
client = SecretClient(vault_url=key_vault_url, credential=credential)

@app.route('/')
def get_secret():
    try:
        # Retrieve the secret
        secret = client.get_secret(SECRET_NAME)
        json_data = json.loads(secret.value)

        # Return the JSON data as an HTTP response
        return jsonify(json_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
