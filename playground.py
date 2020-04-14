import sqlite3
import emoji
import json

# db_file = "./data_repository/dataset.db"
# table = "comment"
# conn = sqlite3.connect(db_file)
# select = f'DELETE FROM {table} WHERE videoId=?'
# # cur = conn.cursor()
# conn.execute(select, ("U_gANjtv28g",))
# # rows = cur.fetchall()
# # for i in rows:
# #     print(emoji.demojize(i[2]))
# conn.commit()
# conn.close()
# with open('./../projectSecrets.json') as json_file:

json_file = open('./../projectSecrets.json')
data = json.load(json_file)
print(data['apiKey'])
json_file.close()
