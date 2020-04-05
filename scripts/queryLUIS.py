from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
import json
import csv

fold = 5

# ----------------------------------------------------------------------
# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

subscription_key = keys['LUIS_subscription_key']
app_id = keys['LUIS_app_id']
runtime_endpoint = 'https://westus.api.cognitive.microsoft.com'

# Instantiate a LUIS runtime client
clientRuntime = LUISRuntimeClient(
    runtime_endpoint, CognitiveServicesCredentials(subscription_key))


def predict(query):

    request = {"query": query}

    response = clientRuntime.prediction.get_slot_prediction(
        app_id=app_id, slot_name='staging', prediction_request=request)

    return response.prediction.top_intent


results = [('Expected', 'Predicted', 'Phrase')]

with open(f'datasetsCV/noEntityFold{fold}Test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        results.append((row[0], predict(row[1]), row[1]))


with open(f'results/noEntityFold{fold}_LUIS.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for result in results:
        writer.writerow(result)
