# This will provide all of the tweets that contain "#python" for the time you start running your script to the time you stop running your script

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Standard Authentication

consumer_key = 'a1RqUEDHSrQ845WOUs4UppDVd'
consumer_secret = '6PHRAN0ey5J4rIigOAornU3IYxJAdasaAmmamQJysDhiP3mTIi'
access_token = '1318630721469042689-5YzlAL2MFzZQ9ySkH8hXGuRFDMzj8I'
access_secret = 'OyQOTIf7HTZqnpDgnwfp4Sb4JEJwit6rTsm0ga1MocBe6'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creates a class that writes the data to a .json file (will return error if there is an error)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('#pythonStreamingData.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
# Will create an instance of MyListener() and will specifically filter for #python references 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

# To see how many tweets gathered, use wc -l #pythonStreamingData.json