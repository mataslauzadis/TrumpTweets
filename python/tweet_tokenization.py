#Takes tweets from donald_trump_tweets.py and 
#1) Breaks the words into tokens, ranking each by frequency 
#2) Plots the frequency using nltk's plot function

import nltk
from nltk.corpus import stopwords
import csv

f = open('donaldTrump.csv','r')
reader = csv.reader(f)

#file = open("tweets.txt", "w", encoding="UTF8")

text='';
rowCount = 3
for row in reader:
	if(row[2] != ''):
		text += row[2].lstrip('b').strip('\'').replace('\\xe2\\x80\\x99','\'').replace('\\xe2\\x80\\x9c','"').replace('\\xe2\\x80\\x9d','"')
		#file.write(row[2]+'\n')
#print(text)
tokens = [t for t in text.split()]
#print(tokens)

sr = stopwords.words('english')
clean_tokens = tokens[:] # The [:] is commonly used to create a copy of the list
for token in tokens: # for x in tokens
	if token in stopwords.words('english') or 'https' in token: #if the word is "the", "and", -OR- contains a twitter link we don't want to evaluate it
		clean_tokens.remove(token)
print(clean_tokens)


freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
	print(str(key) + ':' + str(val))

freq.plot(20,cumulative=False)

