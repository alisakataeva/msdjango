from typing import Optional

from ninja import Schema, ModelSchema

from lib.models import Language


#


class LanguageInSchema(Schema):
    id: Optional[int]
    code: str
    name: str


class LanguageOutSchema(ModelSchema):

    class Config:
        model = Language
        model_fields = "__all__"
