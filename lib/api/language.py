from django.http import HttpRequest
from ninja import Router

from lib.logic.language import create_or_update_language
from lib.schemas.request import SaveLanguageRequest
from lib.schemas.response import LanguageResponse

#


router = Router()


@router.post('/save', response={200: LanguageResponse})
def save_country_endpoint(request: HttpRequest, request_data: SaveLanguageRequest):
    """
    Создание или обновление данных языка
    :param request: HttpRequest
    :param request_data: объект, содержащий данные языка
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и данными языка
    """
    try:
        language = create_or_update_language(request_data.language_data)
        return 200, {
            'code': 'OK',
            'message': 'Информация о языке сохранена успешно',
            'language_data': language
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'language_data': None}
