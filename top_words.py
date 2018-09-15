import matplotlib.pyplot as plt

my_clean_tweets = []
extra_stopwords = []

freq = {}

for tweet in my_clean_tweets:
    words = tweet
    if isinstance(tweet, str):
        tweet = tweet.lower()
        words = tweet.split(' ')

    for word in words:
        count = freq.get(word, 0)
        freq[word] = count + 1

frequency_list = freq.keys()
results = []
for word in frequency_list:
    if min_threshold is not None:
        if freq[word] < min_threshold:
            continue
    tuple = (word, freq[word])
    results.append(tuple)

byFreq = sorted(results, key=lambda word: word[1], reverse=True)

if num_words is not None:
    byFreq = byFreq[: num_words]

if ordered == 'asc':
    byFreq = sorted(byFreq, key=lambda word: word[1], reverse=False)


wfreq = byFreq

words_names = []
words_count = []

need_wfreq = dict()
frequencies = []
total_frequency = 0

for (word, freq) in wfreq:
    if word in extra_stopwords:
        continue
    need_wfreq[word] = freq
    total_frequency += freq
    frequencies.append(freq)

median_freq = 10
## remove low frequency items
final_wfreq = dict()
for word, freq in need_wfreq.items():
    if freq > median_freq:
        final_wfreq[word] = freq

sorted_wfreq = sorted(final_wfreq.items(), key=operator.itemgetter(1))
for word, freq in sorted_wfreq:
    words_names.append(word)
    words_count.append(freq)

print(final_wfreq)

show_plot = True

if show_plot == True:
    #
    fig, ax = plt.subplots()
    width = 0.56 # the width of the bars
    ind = np.arange(len(words_count))  # the x locations for the groups
    ax.barh(ind, words_count, width, color="blue")
    ax.set_yticks(ind+width/2)
    ax.set_yticklabels(words_names, minor=False)
    plt.title('Word Frequency')
    plt.xlabel('Frequencies')
    plt.ylabel('Words')
    for i, v in enumerate(words_count):
        ax.text(v + 0.2, i - .15, str(v), color='blue', fontweight='bold')
    plt.show()
