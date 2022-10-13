from test_package import ngrams
results = [['According', 'to', 'Gran', 'the', 'company', 'has', 'no', 'plans', 'to', 'move', 'all', 'production', 'to', 'Russia'],
           ['According to', 'to Gran', 'Gran the', 'the company', 'company has', 'has no', 'no plans', 'plans to', 'to move', 'move all', 'all production', 'production to', 'to Russia'],
           ['According to Gran', 'to Gran the', 'Gran the company', 'the company has', 'company has no', 'has no plans', 'no plans to', 'plans to move', 'to move all', 'move all production', 'all production to', 'production to Russia'],
           ['According to Gran the', 'to Gran the company', 'Gran the company has', 'the company has no', 'company has no plans', 'has no plans to', 'no plans to move', 'plans to move all', 'to move all production', 'move all production to', 'all production to Russia']]


def test_ngram():
    df = "According to Gran , the company has no plans to move all production to Russia."
    for i in range(1, 4):
        assert ngrams.generate_ngrams(df, i) == results[i - 1]


if __name__ == '__main__':
    test_ngram()
