# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import sqlite3
import googleapiclient.discovery

from sqlite3 import Error
from secretsImport import Secrets


def create_connection(db_file):
    """connect to the database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def add_comments(conn, comment):
    """
    Add a comment to the database
    :param conn: db connection
    :param comment: a list of tuples containing videoId and comment
    """

    insert = '''INSERT INTO comment (videoId, comment)
                VALUES (?,?) '''
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
    DEVELOPER_KEY = Secrets['apiKey']
    videoId = ""

    conn = create_connection("../data_repository/dataset.db")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        videoId=videoId
    )

    while True:
        response = request.execute()
        print(response)
        comment_list = response["items"]

        for comment in comment_list:
            row = (
                comment["snippet"]["videoId"],
                comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"])
            add_comments(conn, row)

        if "nextPageToken" in response.keys():
            request = youtube.commentThreads().list(
                part="snippet",
                pageToken=response['nextPageToken'],
                maxResults=100,
                videoId=videoId
            )
        else:
            break

    conn.close()


if __name__ == "__main__":
    main()
