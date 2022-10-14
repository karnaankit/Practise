import csv
import json
import pandas as pd
from operator import itemgetter
from test_package import ngrams
from collections import defaultdict
from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

count_bigram = defaultdict(int)
count_trigram = defaultdict(int)
with open("urls.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data = row[5]
        data = data.split('--')[0]
        bigram = ngrams.generate_ngrams(data, 2)
        for item1 in bigram:
            count_bigram[item1] += 1
        trigram = ngrams.generate_ngrams(data, 3)
        for item2 in trigram:
            count_trigram[item2] += 1
top_20_bigram = dict(sorted(count_bigram.items(), key=itemgetter(1), reverse=True)[:20])
top_20_trigram = dict(sorted(count_trigram.items(), key=itemgetter(1), reverse=True)[:20])
with open('top_20_bigram.txt', "w") as f:
    f.write(json.dumps(top_20_bigram, indent=4))
with open('top_20_trigram.txt', "w") as f1:
    f1.write(json.dumps(top_20_trigram, indent=4))

topics = defaultdict(list)
with open('urls.csv') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        flag = 0
        flag1 = 0
        data = row[5]
        data = data.split('--')[0]
        trigram = ngrams.generate_ngrams(data, 3)
        for item2 in trigram:
            for state in STATES:
                if similar(state, item2) > 0.5:
                    flag1 = 1
            if flag1 is 1:
                continue
            if item2 in top_20_trigram:
                flag = 1
                if item2 in topics[row[5]]:
                    continue
                topics[row[5]].append(item2)
        bigram = ngrams.generate_ngrams(data, 2)
        flag1 = 0
        for item1 in bigram:
            if flag is 1:
                continue
            for state in STATES:
                if similar(state, item1) > 0.5:
                    flag1 = 1
            if flag1 is 1:
                continue
            if item1 in top_20_bigram:
                if item1 in topics[row[5]]:
                    continue
                topics[row[5]].append(item1)
df1 = pd.DataFrame(topics.items(), columns=['Notes', 'Ngram'])
df = df1[['Ngram', 'Notes']]
df.to_csv('topics.csv')
