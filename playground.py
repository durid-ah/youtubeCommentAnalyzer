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

i = 5
j = 1
while i <= 50:
    print(i, j)
    i += 1
    j += 1
