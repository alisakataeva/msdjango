from ninja import Schema

from lib.schemas.country import CountryInSchema
from lib.schemas.language import LanguageInSchema


#


class SaveCountryRequest(Schema):
    country_data: CountryInSchema


class SaveLanguageRequest(Schema):
    language_data: LanguageInSchema
