from django.http import HttpRequest
from ninja import Router

from common.schemas import BaseJsonResponse
from musicstation.logic.artist import get_artist_data_by_artist_id, get_artist_data_by_artist_slug, \
    get_artist_basic_list, get_favorite_artist_list, get_last_artist_list, create_or_update_artist, delete_artist
from musicstation.schemas.request import GetArtistRequest, GetArtistBasicListRequest, SaveArtistRequest, \
    DeleteArtistRequest
from musicstation.schemas.response import ArtistResponse, ArtistBasicListResponse


#


router = Router()


@router.post('/info', response={200: ArtistResponse})
def get_artist_info_endpoint(request: HttpRequest, request_data: GetArtistRequest):
    """
    Получение информации об исполнителе
    :param request: HttpRequest
    :param request_data: объект, содержащий либо ID исполнителя, либо его SLUG
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и данными об исполнителе
    """
    try:
        if request_data.artist_id is not None:
            artist = get_artist_data_by_artist_id(request_data.artist_id)
        else:
            artist = get_artist_data_by_artist_slug(request_data.artist_slug)
        return 200, {
            'code': 'OK',
            'message': 'Информация об исполнителе получена успешно',
            'artist_data': artist
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'artist_data': None}


@router.post('/all', response={200: ArtistBasicListResponse})
def get_artist_basic_list_endpoint(request: HttpRequest, request_data: GetArtistBasicListRequest):
    """
    Получение упрощенного списка отфильтрованных исполнителей в библиотеке
    :param request: HttpRequest
    :param request_data: объект, содержащий строку, по которой необходимо отфильтровать список по имени исполнителя
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и списком исполнителей
    """
    try:
        res = get_artist_basic_list(request_data.filter_str)
        return 200, {
            'code': 'OK',
            'message': 'Список исполнителей получен успешно',
            'artist_list': res
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'artist_list': None}


@router.post('/favorite', response={200: ArtistBasicListResponse})
def get_artist_favorite_list_endpoint(request: HttpRequest):
    """
    Получение упрощенного списка избранных исполнителей в библиотеке
    :param request: HttpRequest
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и списком избранных исполнителей
    """
    try:
        res = get_favorite_artist_list()
        return 200, {
            'code': 'OK',
            'message': 'Список избранных исполнителей полчен успешно',
            'artist_list': res
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'artist_list': None}


@router.post('/last', response={200: ArtistBasicListResponse})
def get_artist_last_list_endpoint(request: HttpRequest):
    """
    Получение упрощенного списка последних добавленных в библиотеку исполнителей
    :param request: HttpRequest
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и списком последних исполнителей
    """
    try:
        res = get_last_artist_list()
        return 200, {
            'code': 'OK',
            'message': 'Список последних добавленных в библиотеку исполнителей получен успешно',
            'artist_list': res
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'artist_list': None}


@router.post('/save', response={200: ArtistResponse})
def save_artist_endpoint(request: HttpRequest, request_data: SaveArtistRequest):
    """
    Создание или обновление данных исполнителя
    :param request: HttpRequest
    :param request_data: объект, содержащий данные исполнителя
    :return: JSON-объект со строковым кодом результата {OK, ERR}, сообщением и данными исполнителя
    """
    try:
        artist = create_or_update_artist(request_data.artist_data)
        return 200, {
            'code': 'OK',
            'message': 'Информация об исполнителе сохранена успешно',
            'artist_data': artist
        }
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e), 'artist_data': None}


@router.post('/delete', response={200: BaseJsonResponse})
def delete_artist_endpoint(request: HttpRequest, request_data: DeleteArtistRequest):
    try:
        delete_artist(request_data.artist_id)
        return 200, {'code': 'OK', 'message': 'Исполнитель успешно удален'}
    except Exception as e:
        return 200, {'code': 'ERR', 'message': str(e)}
