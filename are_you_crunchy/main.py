from flask import Flask, render_template , jsonify ,request
import json
import tweepy
app = Flask(__name__)

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler('AqaLis4BKx5ONel2LkEYtGcA5', '3Fu9IUKXbkkkzyl4FeYCcgktmJYWTuValRP3cwp7xRGANX8ero')
    auth.set_access_token('80051798-guz9MKxq9EJVeaz0sgF2ZGb43Ey2GhfDvtJG8Q0T5', 'bnLzZEd3bizA2mvu0LWF3Wh37ScdGFjL0bGlP7VNAMF7c')
    api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
    alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=1000)

	#save most recent tweets
    alltweets.extend(new_tweets)

    print alltweets

	#save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

	#transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    tweet_keywords = ['vegetarian', 'vegan', 'natural', 'hippy', 'barefoot', 'healthy', 'natural', 'naked', 'earthy', 'commune', 'nature', 'environment', 'left', 'nature', 'tree', 'hub', 'granola', 'alternative', 'organic', 'green', 'earth', 'environmentally', 'hippies', 'breastfeed', 'left-leaning', 'herbs', 'DIY', 'chicken', 'chickens', 'reusable', 'kombucha', 'recycle', 'reuse', 'reduce', 'coconut', 'compost', 'vegetable', 'grassfed', 'free-range', 'ferment', 'fermented', 'homemade', 'earthy', 'local', 'ethical', 'detox', 'love']

    crunchiness = 0
    for tweet in outtweets:
        tweet_text = tweet[2].lower()
        # return {}
        for keyword in tweet_keywords:
            if tweet_text.find(keyword) != -1:
                crunchiness += 1
    return {'crunchy': crunchiness}


@app.route('/')
def get_crunchy():
    return render_template('index.html')

@app.route('/gettweets/<userid>')
def get_user_tweets(userid):
    res = get_all_tweets(userid)
    return json.dumps(res)

if __name__ == '__main__':
    app.debug = True
    app.run()
