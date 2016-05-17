import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client['crunchy']
Tweets = db['Tweets']

count = {'toffee':0 ,'Jolly Rancher':0,'Starlight peppermint':0,'Corn Nut':0,'Wasabi pea':0,'Grape Nut':0, 'cereal':0,'pretzel':0,'carrot':0,'celery':0,'bell pepper':0,'almond':0,'chips':0,'radish':0,'pickle':0,'biscotti':0,'cracker':0,'tortilla':0 }


dateNow = datetime.datetime.utcnow()

differenceOfMinutes = datetime.timedelta(minutes=1)
neededValueLast1Minutes = dateNow - differenceOfMinutes

last1MinutesData=Tweets.find({"created_at" : { '$gte' : neededValueLast1Minutes }})

for content in last1MinutesData:
	for issue in count.keys():
		if issue in content['text']:
			count[issue] += 1

overView = db['Overview']
result = db.overView.insert_one({"date": dateNow , "count": count} )





