from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.



class Album(models.Model):
  name = models.CharField(max_length=60, unique=True)

  def __str__(self):
    return self.name

class Song(models.Model):
  name = models.CharField(max_length=60, unique=True)
  rating = models.IntegerField(blank = True, null = True, validators= [MaxValueValidator(100), MinValueValidator(0)])
  users = models.ManyToManyField(User, related_name = "songs", related_query_name= "song")
  album = models.ForeignKey(Album, null = True, on_delete= models.SET_NULL)

  def __str__(self):
    return self.name

class Artist(models.Model):
  name = models.CharField(max_length=60, unique=True)
  albums = models.ManyToManyField(Album)

  def __str__(self):
    return self.name


class SongForm(ModelForm):
  class Meta:
    model = Song
    fields = ['name', 'rating']

