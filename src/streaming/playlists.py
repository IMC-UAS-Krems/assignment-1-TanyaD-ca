"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""

from .tracks import Track
from .users import User

class Playlist:
    def __init__(self, playlist_id, title: str, owner=None) -> None:
        self.playlist_id = playlist_id
        self.title = title
        self.owner = owner
        self.tracks: list[Track] = []

    def add_track(self, track: Track) -> None :
        if track not in self.tracks:
            self.tracks.append(track)
    def remove_track(self, track_id: str) -> None:
        new_tracks = []
        for i in self.tracks:
            if i.track_id != track_id:
                new_tracks.append(i)
        self.tracks = new_tracks

    def total_duration_seconds(self) -> int:
        total = 0
        for track in self.tracks:
            total += track.duration_seconds
        return total

class CollaborativePlaylist(Playlist):
    def __init__(self, playlist_id, title: str, owner: User | None = None) -> None:
        super().__init__(playlist_id, title, owner)
        self.contributors: list[User] = []
        if owner is not None:
            self.contributors.append(owner)

    def add_contributor(self, user: User) -> None:
        if user not in self.contributors:
            self.contributors.append(user)

    def remove_contributor(self, user: User) -> None:
        if user != self.owner and user in self.contributors:
            self.contributors.remove(user)