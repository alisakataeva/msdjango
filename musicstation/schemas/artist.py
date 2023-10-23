from typing import Optional

from ninja import ModelSchema, Schema

from musicstation.models import Artist


#


class ArtistInSchema(Schema):
    name: str
    original_name: Optional[str]
    english_name: Optional[str]
    alternative_name: Optional[str]
    country: str
    is_favorite: int


class ArtistOutBasicSchema(ModelSchema):

    class Config:
        model = Artist
        model_fields = ["id", "name", "slug"]


class ArtistOutSchema(ModelSchema):

    class Config:
        model = Artist
        model_fields = "__all__"
