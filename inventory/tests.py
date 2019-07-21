from django.test import TestCase

from .models import Song
# Create your tests here.


class SongModelTests(TestCase):
    def test_song_was_created(self):
        """
        checks that a song was indeed created
        """
        song = Song.objects.create(name="cats")
        self.assertIs(song.name, "cats")
