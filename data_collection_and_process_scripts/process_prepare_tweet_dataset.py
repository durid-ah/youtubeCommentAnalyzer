# grab the tweets from the local database strip out the unnecessary characters
# and create a file with that data to be used in the fasttext training model

from data_repository.sqlite_functions import create_connection
from preprocessing_tools import strip_down_comment

def main():
    tweet_query = "SELECT * FROM labeled_tweet"
    write_file = open('../tweets.txt', 'w', encoding='utf-8')

    conn = create_connection("../data_repository/dataset.db")
    cur = conn.cursor()
    cur.execute(tweet_query)
    rows = cur.fetchall()
    num_rows = len(rows)
    counter = 0

    for item in rows:
        print("Counter: ", counter)
        print(strip_down_comment(item[2]), file=write_file)
        print("Percent: ", (counter / num_rows) * 100, "%")
        counter += 1

    cur.close()
    write_file.close()


if __name__ == "__main__":
    main()
