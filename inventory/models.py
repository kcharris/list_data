from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
  name = models.CharField(max_length=60, unique=True)
  rating = models.IntegerField(default= 0, validators= [MaxValueValidator(100), MinValueValidator(0)])
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
    fields = ['name', 'rating']

