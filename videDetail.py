# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
from secretsImport import Secrets

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    # client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #    client_secrets_file, scopes)
    credentials = Secrets['apiKey']
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=credentials)

    request = youtube.videos().list(
        part="statistics, snippet",
        id="7OGAqaf0kZg"
    )

    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()