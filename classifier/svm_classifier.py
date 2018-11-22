from sklearn.pipeline import Pipeline #pipeline to implement steps in series
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer #convert text comment into a numeric vector
from sklearn.feature_extraction.text import TfidfTransformer #use TF IDF transformer to change text vector created by count vectorizer
from sklearn.svm import SVC# Support Vector Machine
from sklearn.datasets import fetch_20newsgroups


df_train = pd.read_csv("hw_train_2_classes.csv", sep="|")
df_test = pd.read_csv("hw_test_2_classes.csv", sep="|")


#Seperate data into feature and results
X_train, y_train = df_train['tweet'].tolist(), df_train['class'].tolist()
X_test, y_test = df_test['tweet'].tolist(), df_test['class'].tolist()

voc = []
for t in (X_train + X_test):
    terms = t.split()
    voc.extend(terms)

cvec = CountVectorizer(vocabulary=set(voc))

X_train_counts = cvec.fit_transform(X_train)
X_test_counts = cvec.fit_transform(X_test)

#Use pipeline to carry out steps in sequence with a single object
#SVM's rbf kernel gives highest accuracy in this classification problem.
# text_clf = SVC(kernel='rbf')
text_clf = SVC(kernel='linear')

#train model
text_clf.fit(X_train_counts, y_train)

#predict class form test data
predicted = text_clf.predict(X_test_counts)

print(predicted)
print("Accuracy: {}%".format(text_clf.score(X_test_counts, y_test) * 100 ))