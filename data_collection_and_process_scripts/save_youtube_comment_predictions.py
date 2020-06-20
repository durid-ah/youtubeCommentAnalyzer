import fasttext
from data_repository.sqlite_functions import create_connection
from data_collection_and_process_scripts.preprocessing_tools import strip_down_comment


def get_comments(conn):
    query = "SELECT * FROM comment"
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


def insert_prediction(conn, comment_id, label, probability):
    insert = """INSERT INTO prediction (comment_id, label, probability) values (?,?,?)"""

    try:
        conn.execute(insert, (comment_id, label, probability))
        conn.commit()
    except:
        print('An error occurred')


def main():
    model = fasttext.FastText.load_model(
        '../../Documents/Python Scripts/azure_django_apis/sentiment_api/models/sentiment_model_q.ftz'
    )

    conn = create_connection('../data_repository/dataset.db')

    for item in get_comments(conn):
        prediction = model.predict(strip_down_comment(item[2]))
        insert_prediction(conn, item[0], prediction[0][0], prediction[1][0])


if __name__ == '__main__':
    main()
