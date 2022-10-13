from test_package import ngrams


def test_ngram():
    df = "According to Gran , the company has no plans to move all production to Russia."

    def an_vidya(text, ngram):
        text = ngrams.remove_punctuation(text)
        words = text.split()
        temp = zip(*[words[j:] for j in range(0, ngram)])
        ans = [' '.join(ngram) for ngram in temp]
        return ans
    for i in range(1, 4):
        assert ngrams.generate_ngrams(df, i) == an_vidya(df, i)


if __name__ == '__main__':
    test_ngram()
