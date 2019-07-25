from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Song, Album
from .views import *
# Create your tests here.


class SongModelTests(TestCase):
    def setUp(self):
      """
      creates a basic song
      """
      song = Song.objects.create(name='cats')

    def test_no_duplicates_allowed(self):
      """
      makes sure there are no duplicate entries
      """
      with self.assertRaises(IntegrityError):
        song2 = Song.objects.create(name="cats", rating=3)
        
    def test_working_client_post(self):
      """
      tests to make sure the client is sending the correct responses
      """
      c = Client()
      self.assertRedirects(c.post('/inventory/confirmation/', {'name' : 'seventeen', 'rating': '1'}), "/inventory/")

    def test_over_max(self):
      """
      returns error if over max
      """
      c = Client()
      with self.assertRaises(ValueError):
        c.post('/inventory/confirmation/', {'name' : 'seventeen', 'rating': '101'})


    def test_under_min(self):
      "returns error if under min"
      c = Client()
      c.post('/inventory/confirmation/', {'name' : 'seventeen', 'rating': '0'})
      with self.assertRaises(ValueError):
        c.post('/inventory/confirmation/', {'name' : 'seventeen', 'rating': '-1'})

    def test_song_added_to_album(self):
      song = Song.objects.create(name="burgerdance")
      album = Album.objects.create(name="jointeffort")
      song.album = album
      self.assertIs(song.album.name, "jointeffort")
