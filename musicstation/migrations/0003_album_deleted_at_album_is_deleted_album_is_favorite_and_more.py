# Generated by Django 4.2.6 on 2023-10-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicstation', '0002_playlist_album_updated_at_artist_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='album',
            name='is_deleted',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='artist',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='artist',
            name='is_deleted',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='is_deleted',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='is_favorite',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='song',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='song',
            name='is_deleted',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='album',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='song',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего обновления'),
        ),
    ]
