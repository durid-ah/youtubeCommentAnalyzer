# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
from secretsImport import Secrets
from data_repository.sqlite_functions import create_connection

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def add_video(
        conn, video_id, channel_id,
        title, description, thumbnail_url,
        views, likes, dislikes
):
    insert = """
        INSERT INTO video (video_id, channel_id, title, description, thumbnail_url, views, likes, dislikes)
        VALUES (?,?,?,?,?,?,?,?)
    """

    try:
        conn.execute(
            insert, (video_id, channel_id,
            title, description, thumbnail_url,
            views, likes, dislikes)
        )
    except:
        print("An error ocurred")


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    credentials = Secrets['apiKey']
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=credentials)

    request = youtube.videos().list(
        part="statistics,snippet",
        id="g4Hbz2jLxvQ"
    )

    response = request.execute()
    videos = response["items"]
    conn = create_connection("../data_repository/dataset.db")

    for video in videos:
        add_video(
            conn=conn,
            video_id=video['id'],
            channel_id=video['snippet']['channelId'],
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            thumbnail_url=video['snippet']['thumbnails']['default']['url'],
            views=video['statistics']['viewCount'],
            likes=video['statistics']['likeCount'],
            dislikes=video['statistics']['dislikeCount']
        )

    print(response)
    conn.commit()


if __name__ == "__main__":
    main()
