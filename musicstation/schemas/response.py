from typing import Optional

from common.schemas import BaseJsonResponse
from musicstation.schemas.artist import ArtistOutSchema, ArtistOutBasicSchema


#


class ArtistResponse(BaseJsonResponse):
    artist_data: Optional[ArtistOutSchema]


class ArtistBasicListResponse(BaseJsonResponse):
    artist_list: Optional[list[ArtistOutBasicSchema]]
