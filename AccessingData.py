import tweepy
from tweepy import OAuthHandler
import json
 
# Authentication Information
 
consumer_key = 'a1RqUEDHSrQ845WOUs4UppDVd'
consumer_secret = '6PHRAN0ey5J4rIigOAornU3IYxJAdasaAmmamQJysDhiP3mTIi'
access_token = '1318630721469042689-5YzlAL2MFzZQ9ySkH8hXGuRFDMzj8I'
access_secret = 'OyQOTIf7HTZqnpDgnwfp4Sb4JEJwit6rTsm0ga1MocBe6'
 
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




