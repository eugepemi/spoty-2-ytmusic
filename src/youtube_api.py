from typing import Dict, List

from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv()


class YoutubeMusicAPI(object):
    """A class for interacting with the Youtube Music API"""

    def __init__(self) -> None:
        self.yt = YTMusic("oauth.json")

    def _search_songs(self, songs: List[Dict]) -> List[Dict]:
        yt_songs = []
        for s in songs:
            query = f"{s['song']} {s['artist']}"
            search_results = self.yt.search(query, filter="songs", limit=1)
            yt_songs.append(search_results[0])
        return yt_songs

    def migrate_playlist(self, title: str, description: str, songs: List[Dict]) -> None:
        # TODO if playlist already exists?
        yt_songs = self._search_songs(songs)

        return self.yt.create_playlist(
            title=title,
            description=description,
            video_ids=[s["videoId"] for s in yt_songs],
        )
