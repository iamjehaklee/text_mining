from twython import Twython
import pickle
import os


def create_file(filename, query):
    '''
    This function creates a new pickle file containing a list of tweets
    resulting from the input query.
    Inputs: 
        filename - This is the name of the file you want to use to save the tweets in
        query - This is the twitter search query to use to search for tweets and can 
                include operators like AND, OR and NOT, and also 'filter: retweets'
    '''
    # Replace the following strings with your own keys and secrets
    TOKEN = '474185377-n28Q0EN8LQJ1FpEqcyXT8W7SWCv5eyl7DN6vs1VQ'
    TOKEN_SECRET = 'vw5vj6g1DxFEn3mvIBpiuFOfD3n7aepkR1X5tT2lljeUD'
    CONSUMER_KEY = '9OatfUoRO4LpjQBN6du9xXIux'
    CONSUMER_SECRET = 'jeb0amO87oyDKOTw5z5dMlOA4vDpdYlm2POgj7eWe7GgO2cvPv'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

    result = t.search(q=query, count=100, result_type = 'mixed')

    #data = dict()
    tweets = list()
    #tags = list()

    for status in result['statuses']:
        tweets.append(status['text'])
     #   tags.append(status['user']['hashtags'])
    
    # data['tweets'] = tweets
    # data['hashtags'] = tags

    filename += '.pickle'


    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(tweets,f)
        f.close()
        print('File created as %s.' % filename)
    else:
        response = input("File %s already exists. Replace existing? (Y/N):    " % filename)
        if response.lower() == 'y':
            f = open(filename,'wb')
            pickle.dump(tweets,f)
            f.close()
            print('File replaced as %s.' % filename)
        elif response.lower() == 'n':
            print('Action aborted.')


def open_file(filename):
    input_file = open(filename,'rb')
    tweets = pickle.load(input_file)
    input_file.close()
    return tweets


def main():
    create_file('trumptweets', "@realDonaldTrump -filter:retweets")
    create_file('hillarytweets', "@HillaryClinton -filter:retweets")


if __name__ == '__main__':
    main()