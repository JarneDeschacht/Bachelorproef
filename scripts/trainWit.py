import requests
import json

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

url = "https://api.wit.ai/samples"
server_access_token = keys['WIT_server_access_token']
headers = {
    'Authorization': "Bearer {}".format(server_access_token),
    'Content-Type': 'application/json'
}

data = json.dumps([
    {
        "text": "hallo",
        "entities":
        [
            {
                "entity": "intent",
                "value": "greetings"
            }
        ]
    },
    {
        "text": "goeiedag",
        "entities":
        [
            {
                "entity": "intent",
                "value": "greetings"
            }
        ]
    }
])

r = requests.post(url, headers=headers,data=data).json()

print(json.dumps(r, indent=2))

