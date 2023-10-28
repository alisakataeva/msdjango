from typing import Optional

from ninja import ModelSchema, Schema

from musicstation.models import Artist


#


class ArtistInSchema(Schema):
    id: Optional[int]
    name: str
    original_name: Optional[str]
    english_name: Optional[str]
    alternative_name: Optional[str]
    slug: Optional[str]
    searchstring: Optional[str]
    country: str
    is_favorite: int


#


class ArtistOutBasicSchema(ModelSchema):

    class Config:
        model = Artist
        model_fields = ["id", "name", "slug"]


class ArtistOutSchema(ModelSchema):

    class Config:
        model = Artist
        model_fields = "__all__"
