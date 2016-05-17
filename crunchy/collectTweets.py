import tweepy
import sys
import pymongo

#Use your own key, secret, token and token_secret
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().crunchy

    def on_status(self, status):
        #print status.text , "\n"

        data ={}
        data['text'] = status.text
        data['created_at'] = status.created_at
        data['geo'] = status.geo
        data['source'] = status.source

        self.db.Tweets.insert(data)

    # handle errors without closing stream:
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True
sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))

sapi.filter(track=['toffee','Jolly Rancher','Starlight peppermint','Corn Nut','Wasabi pea','Grape Nut', 'cereal','pretzel','carrot','celery','bell pepper','almond','chips','radish','pickle','biscotti','cracker','tortilla'])
