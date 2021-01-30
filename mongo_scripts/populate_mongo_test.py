from secretsImport import Secrets
from pymongo import MongoClient
import datetime

# import datetime as DT
# today = DT.date.today()
# week_ago = today - DT.timedelta(days=7)

# var from = new Date('2014-05-18T20:00:00.000Z');
# var to = new Date('2014-05-19T20:00:00.000Z');
# db.collection.find({startTime: {$gt: from, $lt:to}});

user_name = Secrets["mongo_user"]
password = Secrets["mongo_pass"]
dbname = "durid-tutorial-db"

url = f'mongodb+srv://{user_name}:{password}@cluster0.1uunq.mongodb.net/{dbname}?retryWrites=true&w=majority'
client = MongoClient(url)

db = client['sentiment_analyzer']

db.trends_test.drop()

today = datetime.datetime.utcnow()
one_day = today - datetime.timedelta(days=1)
two_days = today - datetime.timedelta(days=2)
three_days = today - datetime.timedelta(days=3)
four_days = today - datetime.timedelta(days=4)

test_data = [
   *[{'Test': i, 'Time': one_day} for i in range(2)],
   *[{'Test': i, 'Time': two_days} for i in range(8)],
   *[{'Test': i, 'Time': three_days} for i in range(5)],
   *[{'Test': i, 'Time': four_days} for i in range(1)]
]

print("Data to be inserted:")

for i in test_data:
   print(i)

db.trends_test.insert_many(test_data)
