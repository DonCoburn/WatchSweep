from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube"]

def authenticate_youtube():
    """Authenticate and build the YouTube API service."""
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=creds)

def get_watch_later_items(youtube):
    """Fetch videos from the Watch Later playlist."""
    pass
    

def delete_unavailable_videos(youtube):
    """Remove unavailable videos from the Watch Later playlist."""
    pass


if __name__ == "__main__":
    youtube = authenticate_youtube()
    delete_unavailable_videos(youtube)
