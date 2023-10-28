from django.http import Http404
from django.test import TestCase

from common.const import INSTANCE_IS_DELETED
from lib.models import Country
from musicstation.logic.artist import get_artist_data_by_artist_id, get_artist_data_by_artist_slug, \
    get_artist_basic_list, get_favorite_artist_list, get_last_artist_list, create_or_update_artist, delete_artist
from musicstation.models import Artist
from musicstation.schemas.artist import ArtistInSchema


#


def create_country_instance():
    return Country.objects.create(code="ab", name="Ababpa")


class TestArtistLogic(TestCase):

    def test_get_artist_data_by_artist_id(self):

        with self.assertRaises(Http404):
            get_artist_data_by_artist_id(1)

        art = Artist.objects.create(name="Test artist")
        self.assertEqual(get_artist_data_by_artist_id(art.pk), art)

    def test_get_artist_data_by_artist_slug(self):

        with self.assertRaises(Http404):
            get_artist_data_by_artist_slug("test-art")

        art = Artist.objects.create(name="Test artist", slug="test-art")
        self.assertEqual(get_artist_data_by_artist_slug("test-art"), art)

    def test_get_artist_basic_list(self):

        self.assertQuerySetEqual(get_artist_basic_list(None), [])

        art1 = Artist.objects.create(name="Billiano Dmith", searchstring="billiano dmith")
        art2 = Artist.objects.create(name="Billiano Suro", searchstring="billiano suro")
        art3 = Artist.objects.create(name="Bilo Milo", searchstring="bilo milo")
        art4 = Artist.objects.create(name="Cherso Mudiotty", searchstring="cherso mudiotty")
        art5 = Artist.objects.create(name="Hama Rok", searchstring="hama rok")
        art6 = Artist.objects.create(name="Rialo Kawp", searchstring="rialo kawp")
        self.assertQuerySetEqual(get_artist_basic_list(None), Artist.objects.all(), ordered=False)

        self.assertQuerySetEqual(get_artist_basic_list("bil"), [art1, art2, art3], ordered=False)

    def test_get_favorite_artist_list(self):

        self.assertQuerySetEqual(get_favorite_artist_list(), [])

        art1 = Artist.objects.create(name="Billiano Dmith", is_favorite=1)
        art2 = Artist.objects.create(name="Billiano Suro", is_favorite=0)
        self.assertQuerySetEqual(get_favorite_artist_list(), [art1], ordered=False)

    def test_get_last_artist_list(self):

        self.assertQuerySetEqual(get_last_artist_list(), [])

        art1 = Artist.objects.create(pk=3, name="Billiano Dmith")
        art2 = Artist.objects.create(pk=1, name="Billiano Suro")
        self.assertQuerySetEqual(get_last_artist_list(), [art1, art2])

        art3 = Artist.objects.create(pk=5, name="Bilo Milo")
        art4 = Artist.objects.create(pk=28, name="Cherso Mudiotty")
        art5 = Artist.objects.create(pk=13, name="Hama Rok")
        art6 = Artist.objects.create(pk=2, name="Rialo Kawp")
        art7 = Artist.objects.create(pk=4, name="Toh Rmor")
        self.assertQuerySetEqual(get_last_artist_list(), [art4, art5, art3, art7, art1])

    def test_create_or_update_artist(self):

        country_instance = create_country_instance()
        created_instance = create_or_update_artist(
            ArtistInSchema(
                name="Bilo Milo",
                country=country_instance.code,
                is_favorite=0
            )
        )
        self.assertTrue(isinstance(created_instance, Artist))

        updated_instance = create_or_update_artist(
            ArtistInSchema(
                pk=1,
                name="Hama Rok",
                country=country_instance.code,
                is_favorite=1
            )
        )
        self.assertTrue(updated_instance, created_instance)

    def test_delete_artist(self):

        instance = Artist.objects.create(name="Billiano Suro")
        delete_artist(instance.pk)
        deleted_instance = Artist.objects.get(pk=instance.pk)
        self.assertTrue(deleted_instance.is_deleted, INSTANCE_IS_DELETED)
