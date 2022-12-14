import csv
import json
import pandas as pd
from operator import itemgetter
from test_package import ngrams
from collections import defaultdict

STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

state_index = defaultdict(list)
count_bigram = defaultdict(int)
count_trigram = defaultdict(int)
c = int(0)
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
sorted_bigram = sorted(count_bigram.items(), key=itemgetter(1), reverse=True)
sorted_trigram = sorted(count_trigram.items(), key=itemgetter(1), reverse=True)
for state in STATES:
    sorted_bigram = [item for item in sorted_bigram if state.lower() not in item[0].lower()]
    sorted_trigram = [item for item in sorted_trigram if state.lower() not in item[0].lower()]
top_20_bigram = dict(sorted_bigram[:20])
top_20_trigram = dict(sorted_trigram[:20])
with open('top_20_bigram.txt', "w") as f:
    f.write(json.dumps(top_20_bigram, indent=4))
with open('top_20_trigram.txt', "w") as f1:
    f1.write(json.dumps(top_20_trigram, indent=4))

topics = defaultdict(list)
with open('urls.csv') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        flag = 0
        data = row[5]
        data = data.split('--')[0]
        trigram = ngrams.generate_ngrams(data, 3)
        for item2 in trigram:
            if item2 in top_20_trigram:
                flag = 1
                if item2 in topics[row[5]]:
                    continue
                topics[row[5]].append(item2)
        bigram = ngrams.generate_ngrams(data, 2)
        if flag is 1:
            continue
        for item1 in bigram:
            if item1 in top_20_bigram:
                if item1 in topics[row[5]]:
                    continue
                topics[row[5]].append(item1)
df1 = pd.DataFrame(topics.items(), columns=['Notes', 'Ngram'])
df1["State"] = " "
ind = 0
for row in df1.itertuples():
    flag = 0
    unigram = ngrams.generate_ngrams(row[1], 1)
    bigram = ngrams.generate_ngrams(row[1], 2)
    for item in bigram:
        if item in STATES:
            flag = 1
            df1.at[ind, 'State'] = item
            break
    if flag is 1:
        ind += 1
        continue
    for item in unigram:
        if item in STATES:
            df1.at[ind, 'State'] = item
            break
    ind += 1
df = df1[['Ngram', 'State', 'Notes']]
df.to_csv('topics.csv')
