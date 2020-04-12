import requests
import json
import csv

fold = 5

# ----------------------------------------------------------------------

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

client_access_token = keys['Dialogflow_client_access_token']
headers = {
    'Authorization': f'Bearer {client_access_token}',
    'Content-Type': 'application/json'
}


def validateNoEntity():
    results = [('Expected', 'Predicted', 'Phrase')]

    with open(f'datasetsCV/noEntityFold{fold}Test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            url = f'https://api.dialogflow.com/v1/query?lang=nl&sessionId=1&v=20200406&query={row[1]}'
            r = requests.get(url, headers=headers).json()

            try:
                results.append(
                    (row[0], r['result']['metadata']['intentName'], row[1]))
            except:
                results.append((row[0], '', row[1]))

    with open(f'results/noEntityFold{fold}_DIALOGFLOW.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for result in results:
            writer.writerow(result)


def validateEntity():
    results = []

    with open(f'datasetsCV/EntityTest.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            url = f'https://api.dialogflow.com/v1/query?lang=nl&sessionId=1&v=20200406&query={row[1]}'
            r = requests.get(url, headers=headers).json()

            if(r['result']['metadata']):
                if(r['result']['parameters']):
                    results.append({
                        "sentence": row[1],
                        "expectedIntent": row[0],
                        "predictedIntent": r['result']['metadata']['intentName'],
                        "entities": r['result']['parameters']
                    })
                else:
                    results.append({
                        "sentence": row[1],
                        "expectedIntent": row[0],
                        "predictedIntent": r['result']['metadata']['intentName'],
                        "entities": {}
                    })
            else:
                results.append({
                    "sentence": row[1],
                    "expectedIntent": row[0],
                    "predictedIntent": '',
                    "entities": {}
                })

    with open('results/Entity_DIALOGFLOW.json', 'w') as outfile:
        json.dump(results, outfile)


validateEntity()

