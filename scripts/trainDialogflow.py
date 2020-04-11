import requests
import json
import csv

fold = 5

# ----------------------------------------------------------------------

dataset = {}

with open(f'datasetsCV/noEntityFold{fold}Train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        try:
            dataset[row[0]].append(row[1])
        except:
            dataset[row[0]] = []
            dataset[row[0]].append(row[1])

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

url = "https://api.dialogflow.com/v1/intents?lang=nl"
dev_access_token = keys['Dialogflow_developer_access_token']
headers = {
    'Authorization': f'Bearer {dev_access_token}',
    'Content-Type': 'application/json'
}

userSaysObject = []

for intent in dataset:
    for example in dataset[intent]:
        userSaysObject.append({
            "data": [
                {
                    "text": example
                }
            ]
        })

    data = json.dumps({
        "name": intent,
        "auto": True,
        "contexts": [],
        "responses": [],
        "priority": 500000,
        "webhookUsed": False,
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": [],
        "userSays": userSaysObject
    })

    r = requests.post(url, headers=headers, data=data).json()

    print(json.dumps(r, indent=2))

    userSaysObject = []
