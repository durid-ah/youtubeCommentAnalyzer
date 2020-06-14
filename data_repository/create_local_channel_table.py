from data_repository.sqlite_functions import create_connection, create_table


def execute():
    db_name = "./dataset.db"

    create_comments_table = """ CREATE TABLE IF NOT EXISTS channel (
                                    channel_id text PRIMARY KEY,
                                    title text NOT NULL,
                                    thumbnail_url text,
                                    subscribers integer,
                                    videos integer);"""

    conn = create_connection(db_name)
    if conn is not None:
        create_table(conn, create_comments_table)


if __name__ == "__main__":
    execute()
