from pymongo import MongoClient
from pprint import pprint
from secretsImport import Secrets

user_name = Secrets["mongo_user"]
password = Secrets["mongo_pass"]
dbname = "durid-tutorial-db"

url = f'mongodb+srv://{user_name}:{password}@cluster0.1uunq.mongodb.net/{dbname}?retryWrites=true&w=majority'
print(url)

client = MongoClient(url)
print()