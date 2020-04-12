# this code will apply 80/20 principle for the dataset
import json
import csv

from sklearn.model_selection import train_test_split

# load dataset
with open('datasetsCV/datasetNoEntity.json') as ds:
    dataset = json.load(ds)

phrases = []

for intent in dataset.keys():
    for phrase in dataset[intent]:
        phrases.append((intent, phrase))

def writeToCSV(fileName,indexes):
    with open(fileName, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in indexes:
            writer.writerow((i[0],i[1]))

test,train = train_test_split(phrases,shuffle=True,test_size=0.2,train_size=0.8)

writeToCSV(f'datasetsCV/EntityTrain.csv',test)
writeToCSV(f'datasetsCV/EntityTest.csv',train)



