import json
import csv
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

fold = 5

# ----------------------------------------------------------------------
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

def validateNoEntity(): 
    results = [('Expected', 'Predicted', 'Phrase')]

    with open(f'datasetsCV/noEntityFold{fold}Test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # send a query to the assistant
            response = assistant.message(
                assistant_id=assistant_id,
                session_id=session['session_id'],
                input={
                    'message_type': 'text',
                    'text': row[1]
                }
            ).get_result()

            try:
                results.append((row[0], response['output']
                                ['intents'][0]['intent'], row[1]))
            except:
                results.append((row[0], '', row[1]))


    with open(f'results/noEntityFold{fold}_IBMWatson.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for result in results:
            writer.writerow(result)

def validateEntity():

    results = []

    with open('datasetsCV/EntityTest.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # send a query to the assistant
            response = assistant.message(
                assistant_id=assistant_id,
                session_id=session['session_id'],
                input={
                    'message_type': 'text',
                    'text': row[1]
                }
            ).get_result()


            results.append({
                "sentence":row[1],
                "expectedIntent":row[0],
                "predictedIntent":response['output']['intents'][0]['intent'],
                "entities":response['output']['entities']
            })
            # print(json.dumps(usefullResult,indent=2))


    with open('results/Entity_IBMWatson.json', 'w') as outfile:
        json.dump(results, outfile)


# Execute the function
validateEntity()
