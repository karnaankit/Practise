import csv
import json
import pandas as pd
from operator import itemgetter
from test_package import ngrams
from collections import defaultdict


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
        data = row[5]
        data = data.split('--')[0]
        bigram = ngrams.generate_ngrams(data, 2)
        c = 0
        for item1 in bigram:
            if item1 in top_20_bigram:
                if item1 in topics[row[5]]:
                    continue
                topics[row[5]].append(item1)
        trigram = ngrams.generate_ngrams(data, 3)
        for item2 in trigram:
            if item2 in top_20_trigram:
                if item2 in topics[row[5]]:
                    continue
                topics[row[5]].append(item2)
df1 = pd.DataFrame(topics.items(), columns=['Notes', 'Ngram'])
df = df1[['Ngram', 'Notes']]
df.to_csv('topics.csv')
