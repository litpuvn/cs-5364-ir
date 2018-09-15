from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df = pd.read_table('tweets/relevant_tweets.txt')
df.columns = ['tweet']
documents = df['tweet']

query = "love food hurricane harvey texas houston flood road drink water bottle"

tvec = TfidfVectorizer(vocabulary=query.split(' '))
tvec_tfidf = tvec.fit_transform(documents)
tvec_tfidf_as_array = tvec_tfidf.toarray()

print (tvec_tfidf_as_array)

