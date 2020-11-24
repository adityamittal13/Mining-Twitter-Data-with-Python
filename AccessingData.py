import tweepy
from tweepy import OAuthHandler
import json
 
# Authentication Information
 
consumer_key = '*SECRET*'
consumer_secret = '*SECRET*'
access_token = '*SECRET*'
access_secret = '*SECRET*'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# How to get your timeline information (first 10 items)
def printTimelineInfo(num):
	for status in tweepy.Cursor(api.home_timeline).items(num):
	    # Process a single status
	    print(status.text)
	    # For JSON, use json.dumps(status._json)

printTimelineInfo(1)




