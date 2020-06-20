from data_repository.sqlite_functions import create_connection, create_table


def execute():
    db_name = './dataset.db'

    create_prediction_table = """ CREATE TABLE IF NOT EXISTS prediction (
                                    prediction_id integer PRIMARY KEY,
                                    comment_id text NOT NULL,
                                    label text NOT NULL,
                                    probability text
                                  );"""

    conn = create_connection(db_name)
    if conn is not None:
        create_table(conn, create_prediction_table)


if __name__ == '__main__':
    execute()
