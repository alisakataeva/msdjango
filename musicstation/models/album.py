from django.db import models

from musicstation.models import Artist


#


class Album(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    release_date = models.DateField(verbose_name="Дата релиза", null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, verbose_name="Исполнитель", blank=True, null=True,
                               related_name="album_set")

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)

    def __str__(self):
        return self.title
