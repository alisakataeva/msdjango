from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from lib.models import Language
from lib.schemas.language import LanguageInSchema


#


@transaction.atomic
def create_or_update_language(data: LanguageInSchema) -> Language:
    """
    Сохраняет данные языка
    :param data: данные о языке LanguageInSchema
    :return: модель Language
    """

    if data.id is None:
        instance = Language()
        instance.created_at = timezone.now()
    else:
        instance = get_object_or_404(Language, pk=data.id)

    instance.code = data.code
    instance.name = data.name
    instance.save()

    return instance
