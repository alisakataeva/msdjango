from django.db import models

from musicstation.models import Song


#


class Playlist(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=200)
    code = models.CharField(verbose_name="Код", max_length=50, null=True, blank=True, unique=True)
    description = models.CharField(verbose_name="Описание", max_length=1500, null=True, blank=True)
    order = models.PositiveSmallIntegerField(verbose_name="Порядковый номер", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)

    @property
    def songs_count(self):
        if self.playlistsongorder_set != None and self.playlistsongorder_set.count() > 0:
            return self.playlistsongorder_set.count()
        return 0


class PlaylistSongOrder(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, verbose_name="Плейлист",
                                 related_name="playlistsongorder_set")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name="Песня")
    order = models.PositiveSmallIntegerField(verbose_name="Порядковый номер", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)
