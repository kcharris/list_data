from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Song
# Create your tests here.


class SongModelTests(TestCase):
    def setUp(self):
      """
      creates a basic song
      """
      song = Song.objects.create(name = 'cats')
    def test_no_duplicates_allowed(self):
      """
      makes sure there are no duplicate entries
      """
      with self.assertRaises(IntegrityError):
        song2 = Song.objects.create(name= "cats", rating = 3)
    # def test_over_max(self):
    #   """
    #   returns error if over max
    #   """
    #   with self.assertRaises(ValidationError):
    #     Song.objects.update
    # def test_under_min(self):
    #   "returns error if under min"
    #   with self.assertRaises(ValidationError):
    #     song.rating = -1 

