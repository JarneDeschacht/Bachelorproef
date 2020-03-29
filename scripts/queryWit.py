import requests
import json

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

query = "hallo"
url = 'https://api.wit.ai/message?q= {}'.format(query)
client_access_token = keys['WIT_client_access_token']
headers = {
    'Authorization': "Bearer {}".format(client_access_token),
    'Content-Type': 'application/json'
}

r = requests.get(url, headers=headers).json()

print(json.dumps(r, indent=2))
