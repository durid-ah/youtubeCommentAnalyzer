from pymongo import MongoClient
from pprint import pprint

user_name = ""
password = ""
dbname = ""
url = f'mongodb+srv://{user_name}:{password}@cluster0.1uunq.mongodb.net/{dbname}?retryWrites=true&w=majority'