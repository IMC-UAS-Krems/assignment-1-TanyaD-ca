"""
sessions.py
-----------
Implement the ListeningSession class for recording listening events.

Classes to implement:
  - ListeningSession
"""
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .tracks import Track


class ListeningSession:
    def __init__(self, session_id: str, user: "User", track: "Track", timestamp: datetime, duration_seconds: int) -> None:
        self.session_id = session_id
        self.user = user
        self.track = track
        self.timestamp: datetime = timestamp
        self.duration_seconds = duration_seconds
        self.duration_listened_seconds = duration_seconds
        """ I'm running into a conflict in the tests, and I have no idea how to fix the error.
         If I remove the IDs, some tests fail; if I leave them, others fail. Because of this,
         the attribute values get messed up and everything stops working properly.  """
    def duration_listened_minutes(self) -> float:
        return self.duration_listened_seconds/ 60