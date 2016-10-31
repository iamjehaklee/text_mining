import random, pickle, string, nltk, numpy, os
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

def open_file(filename):
    input_file = open(filename,'br')
    tweets = pickle.load(input_file)
    input_file.close()
    return tweets

def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string

    returns: map from each word to the number of times it appears.
    """
    
    hist = {}
    if filename[-7:] == '.pickle':
        raw_data = open_file(filename)

        for line in raw_data:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            for word in line.split():
                # remove punctuation and convert to lowercase
                word = word.strip(strippables)
                word = word.lower()

                # update the histogram
                hist[word] = hist.get(word, 0) + 1        
        return hist
    else:
        fp = open(filename, encoding='utf8')
        for line in fp:
            line = line.replace('-', ' ')
            strippables = string.punctuation + string.whitespace

            for word in line.split():
                # remove punctuation and convert to lowercase
                word = word.strip(strippables)
                word = word.lower()

                # update the histogram
                hist[word] = hist.get(word, 0) + 1

        return hist



def similar(d1, d2):
    """Returns a dictionary with all keys that appear in d1 and d2.

    d1, d2: dictionaries
    """
    result = dict()
    for i in d1:
        if i in d2:
            result[i] = d1[i]
    return result

def finalized_words(x):
    """
    Returns a list of words that have the stop words removed that have been stemmed given a dictionary
    
    x is a dictionary
    returns a dictionary
    """

    st = LancasterStemmer()
    stop = set(stopwords.words('english'))
    result = {}

    for i in x: 
        #Check to see if the word is a stopword. If it is not a stopword, then append it to list 
        if i not in stop:
            stemmed_word = st.stem(i)
            result[stemmed_word] = x[i]
        #Stem the words 
    return result


def most_common(hist, num):
    """Makes a list of word-freq pairs in descending order of frequency. 

    num: the number of results to see.

    hist: map from word to frequency

    returns: list of num (frequency, word) pairs
    """
    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))

    temp.sort()
    temp.reverse()
    return temp[:num]

def write_file(hist, filename):
    '''
    Writes a dictionary to a pickle file.
    filename: string without extension
    hist: dictionary
    '''
    filename += '.pickle'


    if not os.path.exists(filename):
        f = open(filename,'wb')
        pickle.dump(hist,f)
        f.close()
        print('File created as %s.' % filename)
    else:
        response = input("File %s already exists. Replace existing? (Y/N):    " % filename)
        if response.lower() == 'y':
            f = open(filename,'wb')
            pickle.dump(hist,f)
            f.close()
            print('File replaced as %s.' % filename)
        elif response.lower() == 'n':
            print('Action aborted.')

def main():
    input_file1 = open('hillarytweets.pickle','br')
    raw_data1 = pickle.load(input_file1)
    
    hist1 = process_file('hillarytweets.pickle')
    words = process_file('words.txt')

    real_words1 = similar(hist1, words)
    completed_words1 = finalized_words(real_words1)

    print("\n\nThe tokenized words in the Hillary tweets are:")    
    print(completed_words1)

    # write_file(completed_words1, 'tokenizedHillary')

    input_file2 = open('trumptweets.pickle','br')
    raw_data2 = pickle.load(input_file2)
    
    hist2 = process_file('trumptweets.pickle')

    real_words2 = similar(hist2, words)
    completed_words2 = finalized_words(real_words2)

    print("\n\nThe tokenized words in the Trump tweets are:")    
    print(completed_words2)

    print('Most common words in Hillary\'s tweets are:')
    print(most_common(completed_words1, 10))
    print('Most common words in Trump\'s tweets are:')
    print(most_common(completed_words2, 10))

    # write_file(completed_words2, 'tokenizedTrump')


if __name__ == '__main__':
    main()