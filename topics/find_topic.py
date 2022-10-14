import csv
from operator import itemgetter
from test_package import ngrams
topics = set()
count = dict()
file = open("urls.csv")
file1 = open("ngrams.txt", 'w')
file2 = open("note.txt", 'w')
csvreader = csv.reader(file)
for row in csvreader:
    for i in range(0, len(row)):
        bigram = ngrams.generate_ngrams(row[i], 2)
        for item1 in bigram:
            file1.write(item1 + "\n")
            if i is 5:
                file2.write(item1 + "\n")
        trigram = ngrams.generate_ngrams(row[i], 3)
        for item2 in trigram:
            file1.write(item2 + "\n")
            if i is 5:
                file2.write(item2 + "\n")
file1.close()
file2.close()
file1 = open("ngrams.txt", 'r')
for item in file1:
    item = item.rstrip()
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1
file1.close()
top_20 = dict(sorted(count.items(), key=itemgetter(1), reverse=True)[:20])
file2 = open("note.txt", 'r')
for item in file2:
    item = item.rstrip()
    if item in top_20:
        topics.add(item)
file2.close()
print(top_20)
print(topics)
