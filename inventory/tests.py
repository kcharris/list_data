from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Song, Rating
# Create your tests here.


class SongModelTests(TestCase):
    def test_song_was_created(self):
        """
        checks that a song was indeed created
        """
        song = Song.objects.create(name="cats")
        self.assertIs(song.name, "cats")
    def test_no_duplicates_allowed(self):
      """
      makes sure there are no duplicate entries
      """
      with self.assertRaises(IntegrityError):
        song = Song.objects.create(name="cats")
        song2 = Song.objects.create(name= "cats")

class RatingModelTests(TestCase):
  def test_max_validator(self):
    """
    score accepts the max
    """
    rating = Rating.objects.create(score = 100)
    self.assertIs(rating.score, 100)
  def test_over_max(self):
    """
    returns error if over max
    """
    with self.assertRaises(ValidationError):
      rating = Rating.objects.create(score= 102)
  def test_under_min(self):
    "returns error if under min"
    with self.assertRaises(ValidationError):
      rating = Rating.objects.create(score = -1)
      
