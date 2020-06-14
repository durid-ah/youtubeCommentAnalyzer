from data_repository.sqlite_functions import create_connection, create_table


def execute():
    db_name = "./dataset.db"

    create_video_table = """ CREATE TABLE IF NOT EXISTS video (
                                video_id text PRIMARY KEY,
                                channel_id text NOT NULL,
                                title text NOT NULL,
                                description text,
                                thumbnail_url text,
                                views integer,
                                likes integer,
                                dislikes integer);"""

    conn = create_connection(db_name)

    if conn is not None:
        create_table(conn, create_video_table)


if __name__ == "__main__":
    execute()
