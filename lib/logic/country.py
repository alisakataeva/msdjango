from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from lib.models import Country
from lib.schemas.country import CountryInSchema


#


@transaction.atomic
def create_or_update_country(data: CountryInSchema) -> Country:
    """
    Сохраняет данные страны
    :param data: данные о стране CountryInSchema
    :return: модель Country
    """

    if data.id is None:
        instance = Country()
        instance.created_at = timezone.now()
    else:
        instance = get_object_or_404(Country, pk=data.id)

    instance.code = data.code
    instance.name = data.name
    instance.save()

    return instance
