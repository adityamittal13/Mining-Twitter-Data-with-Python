# This allows for simple tokenization using the NLTK tokenization library.

from nltk.tokenize import word_tokenize

#import nltk
#nltk.download('punkt')
 
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(tweet))