import requests
import json

url = 'http://localhost:5005/model/parse'
headers = {
    'Content-Type': 'application/json'
}
data = json.dumps({"text":"hallo"})

r = requests.post(url, headers=headers,data=data).json()

print(json.dumps(r, indent=2))
