# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery

from data_repository.sqlite_functions import create_connection
from secretsImport import Secrets

DEVELOPER_KEY = Secrets['apiKey']


def get_video_ids(conn):
    """
    Get video ids from the video table
    :param conn: the sqlite connection
    :return:
    """
    query = "SELECT video_id FROM video"
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()


def add_comments(conn, comment):
    """
    Add a comment to the database
    :param conn: db connection
    :param comment: a list of tuples containing videoId and comment
    """

    insert = '''INSERT INTO comment (comment_id, video_id, comment, like_count)
                VALUES (?,?,?,?) '''
    try:
        conn.execute(insert, comment)
        conn.commit()
    except:
        print("An error occured")


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    conn = create_connection("../data_repository/dataset.db")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    for id in get_video_ids(conn):

        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=id[0]
        )

        response = request.execute()
        print(response)
        comment_list = response["items"]

        for comment in comment_list:
            row = (
                comment["id"],
                comment["snippet"]["videoId"],
                comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
                comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            )

            add_comments(conn, row)

    conn.close()


if __name__ == "__main__":
    main()
