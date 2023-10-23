from datetime import date
from typing import Optional

from ninja import ModelSchema, Schema

from musicstation.models import Song
from musicstation.schemas.album import AlbumOutBasicSchema
from musicstation.schemas.artist import ArtistOutBasicSchema


#


class SongInSchema(Schema):
    title: str
    original_title: Optional[str]
    english_title: Optional[str]
    romanized_title: Optional[str]
    alternative_title: Optional[str]
    release_date: Optional[date]
    lyrics: Optional[str]
    grade: Optional[int]
    language: str
    artist_id: int
    album_id: int
    number: Optional[int]


class SongOutBasicSchema(ModelSchema):

    class Config:
        model = Song
        model_fields = ["id", "title", "release_date", "grade", "language", "number"]


class SongOutSchema(ModelSchema):
    main_artist: ArtistOutBasicSchema
    album: AlbumOutBasicSchema

    class Config:
        model = Song
        model_fields = "__all__"
