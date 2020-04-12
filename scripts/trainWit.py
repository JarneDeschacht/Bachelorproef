import requests
import json
import csv

# WIT CANNOT HANDLE THE 120 UTTERANCES (DATA GETS LOST, NO ERROR), SPLIT THE DATASET IN 2 TO TRAIN!!!

fold = 5

# ----------------------------------------------------------------------

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

url = "https://api.wit.ai/samples"
server_access_token = keys['WIT_server_access_token']
headers = {
    'Authorization': "Bearer {}".format(server_access_token),
    'Content-Type': 'application/json'
}

formattedDataArr = []

with open(f'datasetsCV/noEntityFold{fold}Train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        formattedDataArr.append({
            "text": row[1],
            "entities":
            [
                {
                    "entity": "intent",
                    "value": row[0]
                }
            ]
        })

r = requests.post(url, headers=headers,
                  data=json.dumps(formattedDataArr)).json()

print(json.dumps(r, indent=2))
