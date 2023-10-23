from datetime import date
from typing import Optional

from ninja import ModelSchema, Schema

from musicstation.models import Playlist, PlaylistSongOrder
from musicstation.schemas.song import SongOutBasicSchema


#


class PlaylistSongOrderInSchema(Schema):
    playlist_id: Optional[int]
    song_id: int
    order: int


class PlaylistInSchema(Schema):
    title: str
    code: Optional[str]
    description: Optional[str]
    order: Optional[int]
    songs_ids: list[PlaylistSongOrderInSchema]


class PlaylistSongOrderOutSchema(ModelSchema):
    song: SongOutBasicSchema

    class Config:
        model: PlaylistSongOrder
        model_fields = ["order", "song"]


class PlaylistOutSchema(ModelSchema):
    playlistsongorder_set: list[PlaylistSongOrderOutSchema]

    class Config:
        model = Playlist
        model_fields = "__all__"
