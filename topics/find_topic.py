import csv
from operator import itemgetter
from test_package import ngrams
from collections import defaultdict

topics = list()
count_bigram = defaultdict(int)
count_trigram = defaultdict(int)
with open("urls.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
            bigram = ngrams.generate_ngrams(row[5], 2)
            for item1 in bigram:
                count_bigram[item1] += 1
            trigram = ngrams.generate_ngrams(row[5], 3)
            for item2 in trigram:
                count_trigram[item2] += 1
top_20_bigram = dict(sorted(count_bigram.items(), key=itemgetter(1), reverse=True)[:20])
top_20_trigram = dict(sorted(count_trigram.items(), key=itemgetter(1), reverse=True)[:20])
with open('top_20_bigram.txt', "w") as f:
    print(top_20_bigram, file=f)
with open('top_20_trigram.txt', "w") as f1:
    print(top_20_trigram, file=f1)
