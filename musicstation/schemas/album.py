from datetime import date
from typing import Optional

from ninja import ModelSchema, Schema

from musicstation.models import Album
from musicstation.schemas.artist import ArtistOutBasicSchema


#


class AlbumInSchema(Schema):
    title: str
    release_date: Optional[date]
    artist_id: int


class AlbumOutBasicSchema(ModelSchema):

    class Config:
        model = Album
        model_fields = ["id", "title", "release_date"]


class AlbumOutSchema(ModelSchema):
    artist: ArtistOutBasicSchema

    class Config:
        model = Album
        model_fields = "__all__"
