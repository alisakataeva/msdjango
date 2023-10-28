from typing import Optional
from ninja import Schema

from musicstation.schemas.artist import ArtistInSchema


#


class GetArtistRequest(Schema):
    artist_id: Optional[int]
    artist_slug: Optional[str]


class GetArtistBasicListRequest(Schema):
    filter_str: Optional[str]


class SaveArtistRequest(Schema):
    artist_data: ArtistInSchema


class DeleteArtistRequest(Schema):
    artist_id: int
