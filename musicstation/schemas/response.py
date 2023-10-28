from common.schemas import BaseJsonResponse
from musicstation.schemas.artist import ArtistOutSchema, ArtistOutBasicSchema


#


class ArtistResponse(BaseJsonResponse):
    artist_data: ArtistOutSchema


class ArtistBasicListResponse(BaseJsonResponse):
    artist_list: list[ArtistOutBasicSchema]
