import pandas as pd

df = pd.read_csv("test.csv", sep=",", header=0)

word_frequency = dict()
class_frequency = dict()
query_x = None
for index, row in df.iterrows():
    tweet = row.iloc[1]
    label = row.iloc[2]

    if "unknown" in label:
        query_x = tweet
        break

    if label not in class_frequency:
        class_frequency[label] = dict()
        class_frequency[label + "-count"] = 0

    current_class = class_frequency[label]
    words = tweet.split()
    for w in words:

        class_frequency[label + "-count"] = class_frequency[label + "-count"] + 1
        if w not in current_class:
            current_class[w] = 0
        current_class[w] = current_class[w] + 1

        if w not in word_frequency:
            word_frequency[w] = 0

        word_frequency[w] = word_frequency[w] + 1

voc_size = len(word_frequency)

for label, word_class_frequency in class_frequency.items():
    if "count" in label:
        continue
    word_count = class_frequency[label + "-count"]
    print("class:", label, "; word count:", word_count)

    x_words = list(set(query_x.split()))
    for w, freq in word_class_frequency.items():
        word_prob = (freq + 1) / (word_count + voc_size)
        print("p(", w, "/", label, ")=", word_prob)

        if w in x_words:
            x_words.remove(w)
    for w in x_words:
        word_prob = (0 + 1) / (word_count + voc_size)
        print("p(", w, "/", label, ")=", word_prob)




