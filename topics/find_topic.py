import csv
from operator import itemgetter
from test_package import ngrams

topics = set()
count = dict()
file = open("urls.csv")
file2 = open("note.txt", 'w')
csvreader = csv.reader(file)
for row in csvreader:
    for i in range(0, len(row)):
        if i is 5:
            bigram = ngrams.generate_ngrams(row[i], 2)
            for item1 in bigram:
                file2.write(item1 + "\n")
            trigram = ngrams.generate_ngrams(row[i], 3)
            for item2 in trigram:
                file2.write(item2 + "\n")
file2.close()
file1 = open("note.txt", 'r')
for item in file1:
    item = item.rstrip()
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1
file1.close()