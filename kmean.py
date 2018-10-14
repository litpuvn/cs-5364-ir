# tutorial  http://madhugnadig.com/articles/machine-learning/2017/03/04/implementing-k-means-clustering-from-scratch-in-python.html
# repository: https://github.com/madhug-nadig/Machine-Learning-Algorithms-from-Scratch/blob/master/K%20Means%20Clustering.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import seaborn as sns
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt, mpld3
from matplotlib import style
style.use('ggplot')

class K_Means:
    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def fit(self, data):
        self.centroids = {}
        # initialize the centroids, the first 'k' elements in the dataset will be our initial centroids
        for i in range(self.k):
            self.centroids[i] = data[i]
        # begin iterations
        for i in range(self.max_iterations):
            self.classes = {}
            for i in range(self.k):
                self.classes[i] = []

            # find the similarity distance between the point and cluster; choose the nearest centroid

            for features in data:
            #    print(features)
              #distances = [np.linalg.norm((features - self.centroids[centroid])) for centroid in self.centroids]
              distances = [self.consine_similarity(features , self.centroids[centroid]) for centroid in self.centroids]
              print(distances)
              classification = distances.index(max(distances))
              print(classification)

              self.classes[classification].append(features)
              previous = dict(self.centroids)
            #print(previous)
            # average the cluster datapoints to re-calculate the centroids
            for classification in self.classes:
                self.centroids[classification] = np.average(self.classes[classification], axis=0)
            isOptimal = True

            for centroid in self.centroids:
                original_centroid = previous[centroid]
                curr = self.centroids[centroid]

                #if np.sum((curr - original_centroid) / original_centroid * 100.0) > self.tolerance:
                 #   isOptimal = False

            # break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
            if isOptimal:
                break

    def consine_similarity(self, vec1, vec2):
       # form vector for similarity
        sim = cosine_similarity(vec1, vec2)
        sim1 = sim[0]
        print(sim1)
        return sim

    # def consine_similarity(raw1, raw2):
    #     attribute_list = []
    #     raw1_attrs = raw1.split()
    #     raw2_attrs = raw2.split()
    #
    #     # form attribute list
    #     for t in (raw1_attrs + raw2_attrs):
    #         if t not in attribute_list:
    #             attribute_list.append(t)

        # # form vector for similarity
        # vec1 = create_binary_vector(raw1_attrs, attribute_list)
        # vec2 = create_binary_vector(raw2_attrs, attribute_list)
        #
        # sim = cosine_similarity([vec1], [vec2])
        # sim1 = sim[0]
        # print(sim1)
        # return sim1[0]


def main():
    df = pd.read_table('tweets/relevant_tweets.txt')
    df.columns = ['tweet']
    documents = df['tweet']
    #print(df)
    # print(documents)
    query = "love food hurricane harvey texas houston flood road drink water bottle"
    tvec = TfidfVectorizer(vocabulary=query.split(' '))
    tvec_tfidf = tvec.fit_transform(documents)
    tvec_tfidf_as_array = np.array(tvec_tfidf.toarray())
    #print(tvec_tfidf_as_array[10111])
    good_documents = []
    for d in tvec_tfidf_as_array:
        if sum(d) >= 0.5:
            good_documents.append(d)
    #print(good_documents)
    X = good_documents
    km = K_Means(3)
    km.fit(X)

    # # Plotting starts here
    # colors = 10 * ["r", "g", "c", "b", "k"]
    #
    # for centroid in km.centroids:
    #     plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], s=130, marker="x")
    #
    # for classification in km.classes:
    #     color = colors[classification]
    #     for features in km.classes[classification]:
    #         plt.scatter(features[0], features[1], color=color, s=30)
    #
    # mpld3.show()

if __name__ == "__main__":
     main()