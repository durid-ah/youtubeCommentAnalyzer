from data_repository.sqlite_functions import create_connection
import pyodbc
from secretsImport import Secrets


def get_channels():
    db_name = '../data_repository/dataset.db'
    channels = 'SELECT * FROM channel'
    conn = create_connection(db_name)
    cursor = conn.cursor()
    cursor.execute(channels)
    return cursor.fetchall()


def main():
    conn_str = 'Driver={ODBC Driver 13 for SQL Server};' + f'Server={Secrets["server"]};' + f'Database={Secrets["database"]};' + f'Uid={Secrets["uid"]};' +  f'Pwd={Secrets["pwd"]};' + 'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    for item in get_channels():
        insert = """INSERT INTO dbo.central_backend_channel (channel_id, title, thumbnail_url, subscribers, videos)
                    VALUES (?,?,?,?,?)"""
        conn.execute(insert, item)
        conn.commit()


if __name__ == '__main__':
    main()
