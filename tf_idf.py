from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords


df = pd.read_csv('tweets/filtered_data.txt', sep="\000")
df.columns =['id', 'tweet_date', 'tweet']

stemmer = SnowballStemmer("english")
stop_words = stopwords.words('english')

## tokenization and remove stopwords
# df['words'] = df['tweet'].apply(lambda x: [item for item in x.split(' ') if item not in stop_words])
df['words'] = df['tweet'].apply(lambda x: ' '.join([word for word in x.split(' ') if word not in stop_words]))

## stem words
df['stemmed'] = df['words'].apply(lambda x: ' '.join([stemmer.stem(y) for y in x.decode('utf-8').split(' ')]))
df['stemmed'].head()
#
#
# ## vectorize with tf-idf
#
# tvec = TfidfVectorizer(min_df=.0025, max_df=.1, stop_words='english', ngram_range=[1, 1])
# tvec_weights = tvec.fit_transform(df.stemmed.dropna())
# weights = np.asarray(tvec_weights.mean(axis=0)).ravel().tolist()
# weights_df = pd.DataFrame({'term': tvec.get_feature_names(), 'weight': weights})
# weights_df.sort_values(by='weight', ascending=False).head(20)