from typing import Optional

from ninja import Schema, ModelSchema

from lib.models import Country


#


class CountryInSchema(Schema):
    id: Optional[int]
    code: str
    name: str


class CountryOutSchema(ModelSchema):

    class Config:
        model = Country
        model_fields = "__all__"
