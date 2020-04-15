# creates a table in the database that contains
# the video comments and their related video id

from data_repository.sqlite_functions import create_connection, create_table


def execute():
    db_name = "./dataset.db"

    create_comments_table = """ CREATE TABLE IF NOT EXISTS comment (
                                    id integer PRIMARY KEY,
                                    videoId text NOT NULL,
                                    comment text);"""

    conn = create_connection(db_name)
    if conn is not None:
        create_table(conn, create_comments_table)


if __name__ == "__main__":
    execute()

