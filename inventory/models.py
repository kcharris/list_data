from django.db import models

# Create your models here.
class Song(models.Model):
  name = models.CharField(max_length=60, unique= True)

class Album(models.Model):
  name = models.CharField(max_length=60, unique= True)
  songs = models.ManyToManyField(Song)

class Artist(models.Model):
  name = models.CharField(max_length=60, unique=True)
  albums = models.ManyToManyField(Album)
