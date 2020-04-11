import requests
import json
import csv

fold = 5

# ----------------------------------------------------------------------

# load file with the secret keys
with open('scripts/keys.json') as f:
    keys = json.load(f)

client_access_token = keys['WIT_client_access_token']
headers = {
    'Authorization': f'Bearer {client_access_token}',
    'Content-Type': 'application/json'
}

results = [('Expected', 'Predicted', 'Phrase')]

with open(f'datasetsCV/noEntityFold{fold}Test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        url = f'https://api.wit.ai/message?q={row[1]}'
        r = requests.get(url, headers=headers).json()

        try:
            results.append((row[0], r['entities']['intent'][0]['value'], row[1]))
        except:
            results.append((row[0], '', row[1]))

with open(f'results/noEntityFold{fold}_WIT.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for result in results:
        writer.writerow(result)
