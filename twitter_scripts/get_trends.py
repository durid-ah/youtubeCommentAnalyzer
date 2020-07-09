import tweepy
import timeit
import json
from secretsImport import Secrets

consumer_key = Secrets["api_key"]
consumer_secret = Secrets["api_secret_key"]
USA_WOEID = 23424977


auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

trends = api.trends_place(USA_WOEID)[0]["trends"][:15]
print("TRENDS:")
print(trends)
print("######################################################")
t = api.search(q="%23Greenleaf", count=100)
for item in t:
    print(item)
# print(json.dumps(t))
print("######################################################")
