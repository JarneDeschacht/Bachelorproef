# code based on https://www.youtube.com/watch?v=gJo0uNL-5Qw
# this code will apply 5 fold cross validation (CV) for the dataset

import json
import csv

# import the library to apply (CV)
from sklearn.model_selection import KFold

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
            writer.writerow(phrases[i])


kf = KFold(n_splits=5, shuffle=True)

counter = 0

for train_index, test_index in kf.split(phrases):
    counter += 1

    print(train_index, test_index)

    writeToCSV(f'datasetsCV/noEntityFold{counter}Train.csv',train_index)
    writeToCSV(f'datasetsCV/noEntityFold{counter}Test.csv',test_index)



