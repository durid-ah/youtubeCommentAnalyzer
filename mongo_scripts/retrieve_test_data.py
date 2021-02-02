from mongo_connection import client
import datetime

today = datetime.datetime.utcnow()
three_days = today - datetime.timedelta(days=3)
db = client['sentiment_analyzer']
vals = db.trends_test.find({'Time': {'$gte': three_days}})

for i in vals:
   print(i)