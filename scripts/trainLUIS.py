from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from msrest.authentication import CognitiveServicesCredentials
import json
import time

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

app_id = keys['LUIS_app_id']
app_version = '0.1'
authoring_endpoint = "https://westus.api.cognitive.microsoft.com"
authoring_key = keys['LUIS_subscription_key']
dataset = {
    'test1': ['test1A', 'test1B', 'test1C'],
    'test2': ['test2A', 'test2B', 'test2C']
}

client = LUISAuthoringClient(
    authoring_endpoint, CognitiveServicesCredentials(authoring_key))


def add_intents():
    for intent in dataset:
        intentId = client.model.add_intent(app_id, app_version, intent)
        print("Intent {} {} added.".format(intent, intentId))


def create_utterance(intent, utterance, *labels):  # labels are optional and skipped atm

    text = utterance.lower()

    def label(name, value):
        value = value.lower()
        start = text.index(value)
        return dict(entity_name=name, start_char_index=start,
                    end_char_index=start + len(value))

    return dict(text=text, intent_name=intent,
                entity_labels=[label(n, v) for (n, v) in labels])


def add_utterances():

    utterances = []

    for intent in dataset:
        for utterance in dataset[intent]:
            utterances.append(create_utterance(intent, utterance))

    print(json.dumps(utterances, indent=2))
    client.examples.batch(app_id, app_version, utterances)
    print("{} example utterance(s) added.".format(len(utterances)))


def train_app():
    response = client.train.train_version(app_id, app_version)
    print("Response from training: {}".format(response))
    waiting = True
    while waiting:
        info = client.train.get_status(app_id, app_version)

        # get_status returns a list of training statuses, one for each model. Loop through them and make sure all are done.
        waiting = any(map(lambda x: 'Queued' ==
                          x.details.status or 'InProgress' == x.details.status, info))
        if waiting:
            print("Waiting 10 seconds for training to complete...")
            time.sleep(10)


def publish_app():
    responseEndpointInfo = client.apps.publish(
        app_id, app_version, is_staging=True)
    print("Application published. Endpoint URL: " +
          responseEndpointInfo.endpoint_url)


add_intents()
add_utterances()
train_app()
publish_app()
