import requests
import json
import csv

fold = 4

# ----------------------------------------------------------------------

url = 'http://localhost:5005/model/parse'
headers = {
    'Content-Type': 'application/json'
}

def validateNoEntity():
    results = [('Expected', 'Predicted', 'Phrase')]

    with open(f'datasetsCV/noEntityFold{fold}Test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = json.dumps({"text": row[1]})
            r = requests.post(url, headers=headers, data=data).json()
            results.append((row[0], r['intent']['name'], row[1]))


    with open(f'results/noEntityFold{fold}_RASA_TEST.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for result in results:
            writer.writerow(result)


def validateEntity():
    results = []

    with open('datasetsCV/EntityTest.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = json.dumps({"text": row[1]})
            r = requests.post(url, headers=headers, data=data).json()
            
            results.append({
                "sentence":row[1],
                "expectedIntent":row[0],
                "predictedIntent":r['intent']['name'],
                "entities":r['entities']
            })

    with open('results/Entity_RASA.json', 'w') as outfile:
        json.dump(results, outfile)


validateEntity()
