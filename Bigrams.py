# This prints out the most common bigrams (sequences of two terms), excluding stopwords

#import nltk
#nltk.download('stopwords')

# OLD PREPROCESS CODE
# Splits up the tweet into hashtags, emoticons, the @ tags, words, punctuation, website URLs
import re
import json

# Regex expressions for emoticons 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
 # Regex expressions for the anatomy of a tweet
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

# Compilation of tokens and emoticons (making it so spaces are ignroed with re.VERBOSE and catch upper and lowercase with re.IGNORECASE)
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
# Finds all of the parts of s that correspond with regex expressions
def tokenize(s):
    return tokens_re.findall(s)
 
# First, finds a list of tokens using tokenize() - if it's not an emoticon, it makes it lowercase
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


from nltk.corpus import stopwords
from nltk import bigrams
import string
import json
from collections import Counter
 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
 
fname = '#pythonStreamingData.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text'].lower()) if term not in stop]
        # Update the counter
        terms_bigram = bigrams(terms_stop)
        count_all.update(terms_bigram)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))