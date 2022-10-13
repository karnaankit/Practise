import string


def remove_punctuation(text):
    if type(text) == float:
        return text
    ans = ""
    for i in text:
        if i not in string.punctuation:
            ans += i
    return ans


def generate_ngrams(text, ngram=2):
    text = remove_punctuation(text)
    final = list()
    ind = 0
    words = text.split()
    for word in words:
        temp = list()
        if len(words) - ind >= ngram:
            temp = words[ind:ngram + ind]
            temp = ' '.join(temp)
            ind += 1
            final.append(temp)
    return final

