import os
from typing import List, Dict
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()


class SpotifyApi(object):
    """
    A class for interacting with the Spotify API

    Attributes:
        sp_client_id (str): The Spotify client ID.
        sp_client_secret (str): The Spotify client secret.
        sp (Spotify): The Spotify API client.
    """

    def __init__(self) -> None:
        self.sp_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.sp_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.sp = self._connect()

    def _connect(self) -> Spotify:
        sp = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self.sp_client_id, client_secret=self.sp_client_secret
            )
        )
        return sp

    def fetch_playlist(self, id: str, fields: str = None) -> Dict:
        return self.sp.playlist(playlist_id=id, fields=fields)

    def tracks_and_artists_of_playlist(self, id: str) -> List[Dict]:
        playlist_response = self.fetch_playlist(
            id=id, fields="tracks.items(track.name, track.artists.name)"
        )
        tracks = playlist_response["tracks"]["items"]
        tracks_names = [
            {
                "song": track["track"]["name"],
                "artist": track["track"]["artists"][0]["name"],
            }
            for track in tracks
        ]
        return tracks_names
