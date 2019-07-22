from django.test import TestCase

from .models import Song, Rating
# Create your tests here.


class SongModelTests(TestCase):
    def test_song_was_created(self):
        """
        checks that a song was indeed created
        """
        song = Song.objects.create(name="cats")
        self.assertIs(song.name, "cats")
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
    rating = Rating.objects.create(score= 101)
    self.assertIs(rating.score, False)
