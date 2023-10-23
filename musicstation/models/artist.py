from django.db import models

from lib.models import Country


#


class Artist(models.Model):
    name = models.CharField(verbose_name="Имя/Псевдоним/Название исполнителя", max_length=50)
    original_name = models.CharField(verbose_name="Имя/Псевдоним/Название исполнителя на оригинальном языке", max_length=50,
                                     null=True, blank=True)
    english_name = models.CharField(verbose_name="Английское Имя/Псевдоним/Название исполнителя", max_length=50, null=True,
                                    blank=True)
    alternative_name = models.CharField(verbose_name="Альтернативное Имя/Псевдоним/Название исполнителя", max_length=50,
                                        null=True, blank=True)
    slug = models.CharField(verbose_name="Уникальный slug исполнителя", max_length=50, null=True, blank=True)
    searchstring = models.CharField(verbose_name="Специальное поле, используемое при поиске", max_length=500, null=True,
                                    blank=True)

    country = models.ForeignKey(Country, to_field='code', on_delete=models.SET_NULL, verbose_name="Страна",
                                null=True, blank=True)
    is_favorite = models.PositiveSmallIntegerField(verbose_name="Избранное", default=0)

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)

    def __str__(self):
        return self.name
