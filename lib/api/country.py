from django.http import HttpRequest
from ninja import Router

from lib.logic.country import create_or_update_country
from lib.schemas.request import SaveCountryRequest
from lib.schemas.response import CountryResponse

#


router = Router()


@router.post('/save', response={200: CountryResponse})
def save_country_endpoint(request: HttpRequest, request_data: SaveCountryRequest):
    """
    Создание или обновление данных страны
    :param request: HttpRequest
    :param request_data: объект, содержащий данные страны
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и данными страны
    """
    try:
        country = create_or_update_country(request_data.country_data)
        return 200, {
            'code': 'OK',
            'message': 'Информация о стране сохранена успешно',
            'country_data': country
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'country_data': None}
