# creates a table of the classified comments

from data_repository.sqlite_functions import create_table, create_connection


def execute():
    db_name = "./dataset.db"

    create_labeled_comments = """ CREATE TABLE IF NOT EXISTS labeled_comment (
                                    id integer PRIMARY KEY,
                                    comment_id integer, 
                                    classified_Comment text NOT NULL,
                                    FOREIGN KEY (comment_id) REFERENCES comment (id));"""

    conn = create_connection(db_name)

    if conn is not None:
        create_table(conn, create_labeled_comments)


if __name__ == "__main__":
    execute()
