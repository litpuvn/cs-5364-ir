from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import codecs
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

df = pd.read_table('tweets/relevant_tweets.txt')
df.columns = ['tweet']
documents = df['tweet']
query = "love food hurricane harvey texas houston flood road drink water bottle"
cvec = CountVectorizer(vocabulary=query.split(' '))
document_term_matrix = cvec.fit_transform(documents)

##  Get the total documents number
tweet_count=0
f = codecs.open('tweets/relevant_tweets.txt', 'rU', 'utf-8')
for line in f:
    tweet_count +=1
print("tweet_count",tweet_count)

## get the document frequency
from collections import defaultdict
import math
##  Get the documents frequency
DF = [0,0,0,0,0,0,0,0,0,0,0]
IDF=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
array_count=0
array_query=[" love "," food "," hurricane"," harvey "," texas"," houston "," flood "," road "," drink "," water ","bottle"]
while array_count<len(array_query):
    with codecs.open('tweets/relevant_tweets.txt', 'rU', 'utf-8') as ins:
      for line in ins:
        if array_query[array_count] in line:
            DF[array_count] += 1
        else:
           continue
        IDF[array_count] = math.log(float(tweet_count) / float(DF[array_count]))
    array_count +=1

print("DF",DF)
print("IDF",IDF)

## plot
fig=plt.figure()
plt.bar(array_query, IDF,0.3,color="green")
plt.xlabel("query terms")
plt.ylabel("IDF")
plt.title("IDF Bar Chart")
plt.show()





