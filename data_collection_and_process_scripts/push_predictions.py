from data_repository.sqlite_functions import create_connection
import pyodbc
from secretsImport import Secrets


def get_videos():
    db_name = '../data_repository/dataset.db'
    channels = 'SELECT comment_id, label, probability FROM prediction WHERE prediction_id <= 2478'
    conn = create_connection(db_name)
    cursor = conn.cursor()
    cursor.execute(channels)
    return cursor.fetchall()


def main():
    conn_str = 'Driver={ODBC Driver 13 for SQL Server};' + f'Server={Secrets["server"]};' + f'Database={Secrets["database"]};' + f'Uid={Secrets["uid"]};' +  f'Pwd={Secrets["pwd"]};' + 'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    conn = pyodbc.connect(conn_str)
    count = 0
    for item in get_videos():
        insert = """INSERT INTO dbo.central_backend_prediction (comment_id, label, probability)
                    VALUES (?,?,?)"""
        conn.execute(insert, item)
        conn.commit()
        count = 1 + count
        print(count)


if __name__ == '__main__':
    main()
