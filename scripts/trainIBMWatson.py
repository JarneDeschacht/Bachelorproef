import json
import csv
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

fold = 5

#----------------------------------------------------------------------
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

api_key = keys['IBM_Watson_API_key']
workspace_id = keys['IBM_Watson_workspace_id']

authenticator = IAMAuthenticator(api_key)
assistant = AssistantV1(
    version='2020-02-05',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')

exampleArr = []

for intent in dataset:
        for example in dataset[intent]:
            exampleArr.append({'text':example})
        
        # Create intent and add training data
        response = assistant.create_intent(
            workspace_id=workspace_id,
            intent=intent,
            examples=exampleArr
        ).get_result()

        print(json.dumps(response, indent=2))

        exampleArr = []




