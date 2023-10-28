from ninja import Schema


#


class BaseJsonResponse(Schema):
    code: str
    message: str
