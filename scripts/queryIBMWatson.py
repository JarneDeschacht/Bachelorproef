import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

assistant_id = keys['IBM_Watson_assistant_id']
api_key = keys['IBM_Watson_API_key']

authenticator = IAMAuthenticator(api_key)

assistant = AssistantV2(
    version='2020-02-05',
    authenticator=authenticator
)

assistant.set_service_url(
    'https://api.eu-gb.assistant.watson.cloud.ibm.com')

# create a session, this will last until there is an inactivity of 5 minutes
session = assistant.create_session(
    assistant_id=assistant_id
).get_result()

# send a message to the assistant
response = assistant.message(
    assistant_id=assistant_id,
    session_id=session['session_id'],
    input={
        'message_type': 'text',
        'text': 'hallo'
    }
).get_result()

print(json.dumps(response, indent=2))
