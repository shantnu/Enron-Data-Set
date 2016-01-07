import nltk.classify.util
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


with open("klay.txt", "r") as f:
    text = f.read()

words = word_tokenize(text)
print(len(words))

freq_dist = nltk.FreqDist(words)

print(freq_dist.most_common(20))