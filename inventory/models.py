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
  users = models.ManyToManyField(User)
  album = models.ForeignKey(Album, null = True, on_delete= models.SET_NULL)

class Artist(models.Model):
  name = models.CharField(max_length=60, unique=True)
  albums = models.ManyToManyField(Album)


class SongForm(ModelForm):
  class Meta:
    model = Song
    fields = ['name', 'rating']

