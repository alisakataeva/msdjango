from common.schemas import BaseJsonResponse
from lib.schemas.country import CountryOutSchema
from lib.schemas.language import LanguageOutSchema


#


class CountryResponse(BaseJsonResponse):
    country_data: CountryOutSchema


class LanguageResponse(BaseJsonResponse):
    language_data: LanguageOutSchema
