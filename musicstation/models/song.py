from django.db import models

from lib.models import Language
from musicstation.models import Artist, Album


#


class Song(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)
    original_title = models.CharField(verbose_name="Название на оригинальном языке", max_length=200, null=True,
                                      blank=True)
    english_title = models.CharField(verbose_name="Название на английском языке", max_length=200, null=True, blank=True)
    romanized_title = models.CharField(verbose_name="Романизированное название", max_length=200, null=True, blank=True)
    alternative_title = models.CharField(verbose_name="Альтернативное название", max_length=200, null=True, blank=True)

    release_date = models.DateField(verbose_name="Дата релиза", null=True, blank=True)
    lyrics = models.TextField(verbose_name="Текст", null=True, blank=True)
    grade = models.PositiveSmallIntegerField(verbose_name="Грейд", null=True, blank=True)
    language = models.ForeignKey(Language, to_field='code', on_delete=models.SET_NULL, verbose_name="Язык", null=True)

    main_artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, verbose_name="Основной исполнитель", blank=True,
                                    null=True, related_name="song_set")
    artist_set = models.ManyToManyField(Artist, verbose_name="Исполнители", blank=True,
                                        related_name="song_set_as_featuring_artist")
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, verbose_name="Альбом", blank=True, null=True,
                              related_name="song_set")
    number = models.PositiveSmallIntegerField(verbose_name="Номер песни в альбоме", null=True, blank=True)

    is_favorite = models.PositiveSmallIntegerField(verbose_name="Избранное", default=0)
    is_deleted = models.PositiveSmallIntegerField(verbose_name="Удалено", default=0)

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name="Дата последнего обновления", null=True, blank=True)
    deleted_at = models.DateTimeField(verbose_name="Дата удаления", null=True, blank=True)
    sorting_title = models.CharField(verbose_name="Служебное название для сортировки", max_length=250, null=True,
                                     blank=True)

    meta = models.TextField(verbose_name="Дополнительная информация", null=True, blank=True)

    def __str__(self):
        return self.title
