Naive Bayes Classifier for Sentiment Analysis

This is a Python implementation of a Naive Bayes Classifier for sentiment analysis, which is the task of determining whether a piece of text expresses a positive or negative sentiment. The implementation uses the Naive Bayes algorithm from the nltk package, and the training data is read from text files.


This code uses the Naive Bayes classifier to perform sentiment analysis on a set of tweets. The tweets are classified as either positive or negative based on the sentiment expressed in the tweet.

Getting Started

Prerequisites

    Python 3.x
    nltk package
Dependencies

This code requires the following dependencies:

    nltk package (Natural Language Toolkit) for natural language processing tasks
    numpy package for numerical computing

To install these packages, you can run the following commands:

pip install nltk
pip install numpy

Running the code

To run the code, simply execute the sentiment_analysis.py file:

python sentiment_analysis.py

This will train the classifier on the training data, and then test it on the test data. The accuracy of the classifier will be printed to the console.
Code Structure

The code consists of several functions and a main script.
Functions

    get_words_in_tweets(tweets): this function takes a list of tweets and returns a list of all the words in the tweets.

    get_word_features(wordlist): this function takes a list of words and returns a list of the most frequent words in the list.

    read_tweets(fname, t_type): this function reads in a file containing tweets and their associated sentiment, and returns a list of tuples containing the tweet text and sentiment.

    extract_features(document): this function takes a list of words and returns a dictionary containing the features of the document.

    classify_tweet(tweet): this function takes a single tweet and returns its sentiment as either 'positive' or 'negative'.


