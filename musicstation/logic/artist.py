from typing import Optional

from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone

from common.const import INSTANCE_IS_DELETED
from lib.models import Country
from musicstation.models import Artist
from musicstation.schemas.artist import ArtistInSchema


#


def get_artist_data_by_artist_id(artist_id: int) -> Artist:
    """
    Возвращает данные исполнителя по его ID
    :param artist_id: ID исполнителя
    :return: модель Artist
    """
    try:
        return get_object_or_404(Artist, pk=artist_id, is_deleted=0)
    except Http404:
        raise Exception("Исполнитель c ID `{}` не найден".format(artist_id))


def get_artist_data_by_artist_slug(artist_slug: str) -> Artist:
    """
    Возвращает данные исполнителя по его SLUG
    :param artist_slug: SLUG исполнителя
    :return: модель Artist
    """
    try:
        return get_object_or_404(Artist, slug=artist_slug, is_deleted=0)
    except Http404:
        raise Exception("Исполнитель c SLUG `{}` не найден".format(artist_slug))


def get_artist_basic_list(filter_str: Optional[str]) -> list[Artist]:
    """
    Возвращает отфильтрованный список исполнителей
    :param filter_str: строка для фильтра по имени
    :return: список моделей Artist
    """
    if filter_str is not None:
        return list(Artist.objects.filter(is_deleted=0, searchstring__icontains=filter_str))
    else:
        return list(Artist.objects.filter(is_deleted=0))


def get_favorite_artist_list() -> list[Artist]:
    """
    Возвращает список избранных исполнителей
    :return: список моделей Artist
    """
    return Artist.objects.filter(is_favorite=1, is_deleted=0)


def get_last_artist_list(quantity: int = 5) -> list[Artist]:
    """
    Возвращает список из <quantity> последних добавленных исполнителей
    :return: список моделей Artist
    """
    return Artist.objects.filter(is_deleted=0).order_by("-id")[:quantity]


@transaction.atomic
def create_or_update_artist(data: ArtistInSchema) -> Artist:
    """
    Сохраняет данные исполнителя
    :param data: данные об исполнителе ArtistInSchema
    :return: модель Artist
    """

    if data.id is None:
        instance = Artist()
        instance.created_at = timezone.now()
    else:
        try:
            instance = get_object_or_404(Artist, pk=data.id)
        except Http404:
            raise Exception("Исполнитель c ID `{}` не найден".format(data.id))

    instance.name = data.name
    instance.slug = data.slug
    instance.searchstring = data.searchstring

    instance.original_name = data.original_name
    instance.english_name = data.english_name
    instance.alternative_name = data.alternative_name

    try:
        instance.country = get_object_or_404(Country, code=data.country)
    except Http404:
        raise Exception("Страна c кодом `{}` не найдена".format(data.country))

    instance.is_favorite = data.is_favorite if data.is_favorite is not None else 0
    instance.is_deleted = data.is_deleted if data.is_deleted is not None else 0

    instance.updated_at = timezone.now()
    instance.save()

    return instance


@transaction.atomic
def delete_artist(artist_id: int):
    """
    Помечает исполнителя как удаленного
    :param artist_id: ID исполнителя
    :return:
    """
    try:
        instance = get_object_or_404(Artist, pk=artist_id, is_deleted=0)
    except Http404:
        raise Exception("Исполнитель c ID `{}` не найден".format(artist_id))
    instance.is_deleted = INSTANCE_IS_DELETED
    instance.deleted_at = timezone.now()
    instance.save()
