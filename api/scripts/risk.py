import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define a list of training sentences that are labeled with their associated suicide risk level
training_data = [("I feel hopeless and alone", 1),
                 ("Life is not worth living anymore", 1),
                 ("I want to end my life", 1),
                 ("I am feeling depressed", 0),
                 ("I had a bad day at work", 0),
                 ("I'm really stressed out", 0)]

# Convert the training data into a pandas dataframe
df = pd.DataFrame(training_data, columns=["text", "suicide_risk"])

# Convert the text data into a matrix of word frequencies using a CountVectorizer
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["text"])

# Train a Naive Bayes classifier on the word frequency data
clf = MultinomialNB().fit(X, df["suicide_risk"])

# Define a function to predict the suicide risk level of a given sentence
def predict_suicide_risk(text):
    # Convert the text data into a matrix of word frequencies using the same vectorizer as before
    X_test = vectorizer.transform([text])
    
    # Use the trained classifier to predict the likelihood of suicide risk for the given sentence
    y_pred = clf.predict_proba(X_test)
    
    # Return the predicted suicide risk level
    print(y_pred[0][1])

predict_suicide_risk("I want to die!")