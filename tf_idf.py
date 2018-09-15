from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords


df = pd.read_csv('tweets/clean_tweets.csv', sep=',', encoding="utf-8")
df.columns =['id','tweet']

## vectorize with tf-idf

tvec = TfidfVectorizer(min_df=.0025)
tvec_weights = tvec.fit_transform(df['tweet'])
weights = np.asarray(tvec_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': tvec.get_feature_names(), 'weight': weights})
weights_df.sort_values(by='weight', ascending=False).head(20)

print("done")