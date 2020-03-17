from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
import json

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

subscription_key = keys['LUIS_subscription_key']
app_id = keys['LUIS_app_id']
runtime_endpoint = 'https://westus.api.cognitive.microsoft.com'
query = 'hallo'

# Instantiate a LUIS runtime client
clientRuntime = LUISRuntimeClient(
    runtime_endpoint, CognitiveServicesCredentials(subscription_key))


def predict(app_id):

    request = {"query": query}

    response = clientRuntime.prediction.get_slot_prediction(
        app_id=app_id, slot_name='staging', prediction_request=request)

    print("Intent: {}".format(response.prediction.top_intent))


predict(app_id)
