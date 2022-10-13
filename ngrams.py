df="According to Gran , the company has no plans to move all production to Russia."

import string
string.punctuation

def remove_punctuation(text):
  if(type(text)==float):
    return text
  ans=""  
  for i in text:     
    if i not in string.punctuation:
      ans+=i    
  return ans

df= remove_punctuation(df)

def generate_ngrams(text, ngram=2):
  ind=0
  words=text.split()
  for word in words:
    temp = list()
    if len(words)-ind >= ngram:   
      temp=words[ind:ngram+ind]
      temp=' '.join(temp)
      ind+=1
      print(temp)

print(generate_ngrams(df,3))

