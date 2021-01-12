import fasttext
from data_repository import sqlite_functions

model = fasttext.load_model('sentiment_model.bin')
result = model.predict("terrible")
print(result)
