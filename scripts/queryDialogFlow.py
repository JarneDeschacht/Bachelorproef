import requests
import json

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

url = 'https://api.dialogflow.com/v1/query?lang=nl&sessionId=1&v=20170712&query=hallo&timezone=Europe/Brussels'
client_access_token = keys['Dialogflow_client_access_token']
headers = {
    'Authorization': "Bearer {0}".format(client_access_token),
    'Content-Type': 'application/json'
}

r = requests.get(url, headers=headers).json()

print(json.dumps(r, indent=2))
