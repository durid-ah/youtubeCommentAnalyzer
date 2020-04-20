# creates a table of the classified tweets

from data_repository.sqlite_functions import create_table, create_connection


def execute():
    db_name = "./dataset.db"

    create_labeled_tweets = """ CREATE TABLE IF NOT EXISTS labeled_tweet (
                                    id integer PRIMARY KEY,
                                    target integer, 
                                    classified_tweet text NOT NULL);"""

    conn = create_connection(db_name)

    if conn is not None:
        create_table(conn, create_labeled_tweets)


if __name__ == "__main__":
    execute()
