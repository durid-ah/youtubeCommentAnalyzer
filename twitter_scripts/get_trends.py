import tweepy
import timeit
import json
from secretsImport import Secrets

# ['id'] ......................... The tweet's id
# ['text'] ....................... The content of the tweet
# ['user']['screen_name'] ........ The users screen name (@)
# ['user']['profile_image_url'] .. The users profile image
# ['retweet_count'] .............. The post's (tweet) number of retweets
# ['favorite_count'] ............. The number of times this post (tweet) has been favorited


def filter_twitter_statuses(status):
    return {
        'id': status['id'],
        'text': status['text'],
        'screen_name': status['user']['screen_name'],
        'profile_image_url': status['user']['profile_image_url'],
        'retweet_count': status['retweet_count'],
        'favorite_count': status['favorite_count']
    }

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

# for item in t['statuses']:
#     print(item)
print("######################################################")

new_trends = list(
    map(
        lambda status: {
            'id': status['id'],
            'text': status['text'],
            'screen_name': status['user']['screen_name'],
            'profile_image_url': status['user']['profile_image_url'],
            'retweet_count': status['retweet_count'],
            'favorite_count': status['favorite_count'] }
        , t['statuses'])
)
print(new_trends)
