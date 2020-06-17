from data_repository.sqlite_functions import create_connection

def get_video_ids(conn):
    query = "SELECT video_id FROM video"
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


if __name__ == '__main__':
    conn = create_connection("./data_repository/dataset.db")
    rows = get_video_ids(conn)
    for i in rows:
        print(f'{i[0]} :: {type(i)}')
