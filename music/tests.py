from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse


from .views import AccountMusicList
from .models import Song, Album, UserRating
# Create your tests here.


class SongModelTests(TestCase):
    def setUp(self):
        """
        creates a basic song
        """
        Song.objects.create(name='cats')

    def test_no_duplicates_allowed(self):
        """
        makes sure there are no duplicate entries
        """
        with self.assertRaises(IntegrityError):
            Song.objects.create(name="cats", rating=3)

    def test_working_client_post(self):
        """
        tests to make sure the client is sending the correct responses
        """
        c = Client()
        self.assertRedirects(c.post('/music/confirmation/',
                                    {'name': 'seventeen', 'rating': '1'}), reverse('music_list'))

    def test_over_max(self):
        """
        returns error if over max
        """
        c = Client()
        with self.assertRaises(ValueError):
            c.post('/music/confirmation/',
                   {'name': 'seventeen', 'rating': '101'})

    def test_under_min(self):
        "returns error if under min"
        c = Client()
        c.post('/music/confirmation/',
               {'name': 'seventeen', 'rating': '0'})
        with self.assertRaises(ValueError):
            c.post('/music/confirmation/',
                   {'name': 'seventeen', 'rating': '-1'})

    def test_song_added_to_album(self):
        song = Song.objects.create(name="burgerdance")
        album = Album.objects.create(name="jointeffort")
        song.album = album
        self.assertIs(song.album.name, "jointeffort")

    def test_songs_arent_deleted_with_album(self):
        album = Album.objects.create(name="a")
        album.save()
        for x in range(5):
            song = Song.objects.create(name=f"song{x}")
            song.album = Album.objects.get(name="a")
            song.save()
        song2 = Song.objects.get(name="song2")
        album.delete()
        self.assertIn(song2, Song.objects.all())


class AccountItemListViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="testuser", password="testpassword").save()

    def test_user_signed_in(self):
        c = Client()
        c.login(username="testuser", password="testpassword")
        response = c.get("/music/accounts_list/")
        self.assertEqual(response.resolver_match.func.__name__,
                         AccountMusicList.as_view().__name__)


class UserRatingModel(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="testuser", password="testpassword").save()
        for x in range(5):
            song = Song.objects.create(name= str(x))
            song.user = User.objects.get(username="testuser")
            UserRating.objects.create(user=song.user, song=song)

    def test_change_user_rating(self):
        song = Song.objects.get(name = "1")
        rating = UserRating.objects.get(song=song)
        rating.rating = 99
        rating.save()
        self.assertEqual(99, UserRating.objects.get(song=song).rating)
