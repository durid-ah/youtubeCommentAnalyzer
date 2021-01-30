from secretsImport import Secrets
from pymongo import MongoClient

user_name = Secrets["mongo_user"]
password = Secrets["mongo_pass"]
dbname = "durid-tutorial-db"

url = f'mongodb+srv://{user_name}:{password}@cluster0.1uunq.mongodb.net/{dbname}?retryWrites=true&w=majority'
client = MongoClient(url)