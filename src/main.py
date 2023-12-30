import os

from dotenv import load_dotenv

from spotify_api import SpotifyAPI
from youtube_api import YoutubeMusicAPI

load_dotenv()

MANDATORY_ENV_VARS = [
    "SPOTIFY_CLIENT_ID",
    "SPOTIFY_CLIENT_SECRET",
    "SPOTIFY_PLAYLIST_ID",
    "YT_PLAYLIST_NAME",
    "YT_PLAYLIST_DESCRIPTION",
]

if __name__ == "__main__":
    for var in MANDATORY_ENV_VARS:
        if var not in os.environ:
            raise EnvironmentError(f"{var} not found in environment variables")

    spotify_api = SpotifyAPI()
    youtube_api = YoutubeMusicAPI()
    playlist = os.getenv("SPOTIFY_PLAYLIST_ID")

    youtube_api.migrate_playlist(
        title=os.getenv("YT_PLAYLIST_NAME"),
        description=os.getenv("YT_PLAYLIST_DESCRIPTION"),
        songs=spotify_api.get_songs_names_artists(playlist),
    )
