import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


def get_words_in_tweets(tweets):
    return [word for (words, sentiment) in tweets for word in words]


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    return wordlist.keys()


def read_tweets(fname, t_type):
    with open(fname, 'r') as f:
        tweets = [[line.strip(), t_type] for line in f]
    return tweets


def extract_features(document):
    document_words = set(document)
    features = {'contains(%s)' % word: (word in document_words) for word in word_features}
    return features


def classify_tweet(tweet):
    return classifier.classify(extract_features(nltk.word_tokenize(tweet)))


pos_tweets = read_tweets('happy.txt', 'positive')
neg_tweets = read_tweets('sad.txt', 'negative')

tweets = [([e.lower() for e in words.split() if len(e) >= 3], sentiment) for (words, sentiment) in pos_tweets + neg_tweets]

word_features = get_word_features(get_words_in_tweets(tweets))

training_set = nltk.classify.util.apply_features(extract_features, tweets)
classifier = NaiveBayesClassifier.train(training_set)

test_tweets = read_tweets('happy_test.txt', 'positive') + read_tweets('sad_test.txt', 'negative')
total = accuracy = float(len(test_tweets))

for tweet in test_tweets:
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1

print('Total accuracy: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
