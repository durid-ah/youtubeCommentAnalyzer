import sqlite3

db_file = "./dataset.db"
table = "comment"
conn = sqlite3.connect(db_file)
delete = f'DELETE FROM {table}'
conn.execute(delete)
conn.commit()
conn.close()
