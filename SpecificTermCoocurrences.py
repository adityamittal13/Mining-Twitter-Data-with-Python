# Catching term re-occurrences where the two terms are frequently in the same tweet
# Different from bigrams as bigrams often have to be together

from collections import defaultdict
import operator
import json # necessary for extracting the JSON file containing the Python info
from collections import Counter # keeping track of all the frequencies
import re # joining necessary parts like hashtags and emotes together
import string
from nltk import bigrams # will take a list of tokens and produce a list of tuples using adjacent tokens
import sys

import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords # explicitly for removing stop words
 
com = defaultdict(lambda : defaultdict(int))
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'RT', '...', '1', 'via']

# Catching for certain emoticons so that it doesn't split
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
# Catching additional keywords (like URLs and hash-tags)
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
 
# Allowing spaces to be ignored and catching uppercases/lowercases  
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

# Catching all tokens in a string and returns as a list
def tokenize(s):
    return tokens_re.findall(s)
 
# Making sure that emoticons are not lowercased
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

fname = '#pythonStreamingData.json'
with open(fname, 'r') as f:
    search_word = sys.argv[1] # pass a term as a command-line argument
    count_search = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text']) 
                      if term not in stop 
                      and not term.startswith(('#', '@'))]
        if search_word in terms_only:
            count_search.update(terms_only)
print("Co-occurrence for %s:" % search_word)
print(count_search.most_common(20))