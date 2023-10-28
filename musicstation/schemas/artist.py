from typing import Optional

from ninja import ModelSchema, Schema, Field

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
    is_favorite: Optional[int]
    is_deleted: Optional[int]


#


class ArtistOutBasicSchema(ModelSchema):

    class Config:
        model = Artist
        model_fields = ["id", "name", "slug"]


class ArtistOutSchema(ModelSchema):
    country: str = Field(None, alias="country.code")

    class Config:
        model = Artist
        model_fields = "__all__"
