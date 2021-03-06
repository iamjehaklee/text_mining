from Tokenization import *
import nltk
# from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def create_text(hist):
    '''
    converts dictionary to string based on word frequencies.
    Keys = String words
    Value = Int word frequencies
    '''
    result = str()
    for i in hist:
        for j in range(hist[i]):
            result = result + ' ' + i
    return result

def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def sentiments(text):
    '''
    This compiles a list of sentiment results of each tweet in text.
    text: list of tweets
    '''
    result = []
    for tweet in text:
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        result.append(score)

    return result

def positivity(x):
    pos = float()
    for i in x:
        pos += i['pos']
    pos = pos/len(x)
    return pos

def negativity(x):
    neg = float()
    for i in x:
        neg += i['neg']
    neg = neg/len(x)
    return neg


def main():
    trump = open_file('trumptweets.pickle')
    hillary = open_file('hillarytweets.pickle')

    trumps = sentiments(trump)
    hillarys = sentiments(hillary)

    write_file(trumps, 'sentiments_trump')
    write_file(hillarys, 'sentiments_hillary')

    print('Average positivity in Trump\'s tweets:', end=" ")
    print(positivity(trumps))
    print('Average positivity in Hillary\'s tweets:', end=" ")
    print(positivity(hillarys))

    print('Average negativity in Trump\'s tweets:', end=" ")
    print(negativity(trumps))
    print('Average negativity in Hillary\'s tweets:', end=" ")
    print(negativity(hillarys))


    # print(cosine_sim(trumpwords, hillarywords))


if __name__ == '__main__':
    main()