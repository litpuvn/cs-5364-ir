from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../aid_request/processed_count_vector_predicted.csv', sep="|", quotechar='"', header=0)
text = []
for index, row in df.iterrows():
    tweet_id = row['tweet_id']
    tweet = row['tweet']
    actual_label = row['label']
    predicted_label = row['predicted_class']

    if predicted_label == 0:
        text.append(tweet)


# Generate a word cloud image
wordcloud = WordCloud(background_color="black", collocations=False).generate(' '.join(text))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

