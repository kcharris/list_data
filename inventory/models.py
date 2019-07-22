from django.db import models
from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Rating(models.Model):
  score = models.IntegerField(verbose_name= 0, validators=[validators.MaxValueValidator(100), validators.MinValueValidator(0)])


class Song(models.Model):
  name = models.CharField(max_length=60, unique=True)
  rating = models.ManyToManyField(Rating)
  users = models.ManyToManyField(User)


class Album(models.Model):
  name = models.CharField(max_length=60, unique=True)
  songs = models.ManyToManyField(Song)


class Artist(models.Model):
  name = models.CharField(max_length=60, unique=True)
  albums = models.ManyToManyField(Album)


class SongForm(ModelForm):
  class Meta:
    model = Song
    fields = ['name']

class RatingForm(ModelForm):
  class Meta:
    model = Rating
    fields = ['score']
