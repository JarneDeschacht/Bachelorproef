import json
import csv
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

with open('noEntityFold1Train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'{row[0]} : {row[1]}')

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

# Create intent and add training data
response = assistant.create_intent(
    workspace_id=workspace_id,
    intent='test2',
    examples=[
        {'text': 'test1'},
        {'text': 'test2'}
    ]
).get_result()

print(json.dumps(response, indent=2))
