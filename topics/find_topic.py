import csv
from operator import itemgetter
from test_package import ngrams
from collections import defaultdict

topics = list()
count_bigram = defaultdict(int)
count_trigram = defaultdict(int)
file = open("urls.csv")
csvreader = csv.reader(file)
for row in csvreader:
        bigram = ngrams.generate_ngrams(row[5], 2)
        for item1 in bigram:
            count_bigram[item1] += 1
        trigram = ngrams.generate_ngrams(row[5], 3)
        for item2 in trigram:
            count_trigram[item2] += 1
file.close()
