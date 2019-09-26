from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
  name = models.CharField(blank = False, max_length = 20)

class Item(models.Model):
  name = models.CharField(blank = False, max_length = 100)

class List(models.Model):
  name = models.CharField(blank = False, unique = True, max_length= 60)
  items = models.ManyToManyField(Item, related_name = "items")
  tags = models.ManyToManyField(Tag, related_name= "tags")
