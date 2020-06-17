# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from data_repository.sqlite_functions import create_connection
from secretsImport import Secrets

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def add_channel(conn, channel_id, title, thumbnail_url, subscribers, videos):
    insert = """INSERT INTO channel (channel_id, title, thumbnail_url, subscribers, videos) 
                VALUES (?,?,?,?,?)"""

    try:
        conn.execute(insert, (channel_id, title, thumbnail_url, subscribers, videos))
        conn.commit()
    except:
        print("An error occured")


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    credentials = Secrets['apiKey']
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=credentials)

    request = youtube.channels().list(
        part="statistics,snippet",
        id="UCz97F7dMxBNOfGYu3rx8aCw",
        maxResults=50
    )
    response = request.execute()
    channel = response['items'][0]
    conn = create_connection("../data_repository/dataset.db")

    print(response)
    add_channel(
        conn=conn,
        channel_id=channel['id'],
        title=channel['snippet']['title'],
        thumbnail_url=channel['snippet']['thumbnails']['default']['url'],
        videos=channel['statistics']['videoCount'],
        subscribers=channel['statistics']['subscriberCount']
    )


if __name__ == "__main__":
    main()
