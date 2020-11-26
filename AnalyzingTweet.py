# This will take all of the tweets recorded from StreamingData.py and put them inside the console in an easier-to-read format

import json
 
with open('#pythonStreamingData.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print