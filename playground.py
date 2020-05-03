import sqlite3
import emoji
import json
import pandas as pd

# db_file = "./data_repository/dataset.db"
# table = "comment"
# conn = sqlite3.connect(db_file)
# select = f'SELECT * FROM {table} WHERE id=?'
# cur = conn.cursor()
# cur.execute(select, (2247,))
# rows = cur.fetchall()
# for i in rows:
#     text = TextBlob(i[2])
#     print(text.sentiment)
#     print(text.sentiment_assessments)
# conn.commit()
# conn.close()

# with open('./../projectSecrets.json') as json_file:

# json_file = open('./../projectSecrets.json')
# data = json.load(json_file)
# print(data['apiKey'])
# json_file.close()

# headers = ['target', 'id', 'date', 'flag', 'user', 'text']
#
# df = pd.read_csv(
#     '../Downloads/sentiment140/training.1600000.processed.noemoticon.csv',
#     encoding='latin1',
#     names=headers
# )
#
# print(df)

# i = 5
# j = 1
# while i <= 50:
#     print(i, j)
#     i += 1
#     j += 1

from sklearn.model_selection import train_test_split

f = open('yelp.split.test', 'w+')
x = f.readlines()
print("Files are read...")


x[(len(x) - 1)] = (x[ (len(x) - 1)]).replace('__label', '\n__label')
f.write(''.join(x))
f.close()
# print("Closing file and splitting set...")
# X_train, X_test = train_test_split(x, test_size=0.17, random_state=42)
# del x
# print("Set split up")
# wftr = open('yelp.split.train', 'w+')
# count = 0
# for item in X_train:
#     print("Writing train %", count / (6685899 * 0.83))
#     wftr.write(item.replace('\n', '') +'\n')
#     count += 1
#
# wftr.close()
# del X_train
# count = 0
# wfte = open('yelp.split.test', 'w+')
# for item in X_test:
#     print(" Writing test %", count / (6685899 * 0.17))
#     wfte.write(item.replace('\n', ''))
#     count += 1
#
# wfte.close()
