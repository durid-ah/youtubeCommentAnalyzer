from secretsImport import Secrets
from pymongo import MongoClient
from datetime import datetime

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

db = client['sentiment']
db.trends.insert_many([{}])
