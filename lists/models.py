from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
  name = models.CharField(blank = False, max_length = 20)

  def __str__(self):
    return self.name

class Item(models.Model):
  name = models.CharField(blank = False, max_length = 100)
  tag_values = models.ManyToManyField(Tag, through= "ItemTagValue")

  def __str__(self):
    return self.name


class List(models.Model):
  #In order for each item in the list to have a required name. The item object will use it's name like the the first tag in a row of tags.
  #For example ["Name"str][tag     ][tag     ][tag     ]
  #            [Item     ][item.tag][item.tag][item.tag]
  name = models.CharField(blank = False, unique = True, max_length= 60)
  items = models.ManyToManyField(Item, related_name = "lists", related_query_name= "list")
  tags = models.ManyToManyField(Tag, related_name= "lists", related_query_name= "list")
  users = models.ManyToManyField(User)

  def get_absolute_url(self):
    return reverse('list-detail', kwargs={'pk': self.pk}) # modify urls to comply

  def __str__(self):
    return self.name

class ItemTagValue(models.Model):
  tag = models.ForeignKey(Tag, on_delete= models.CASCADE)
  item = models.ForeignKey(Item, on_delete= models.CASCADE)
  inventory = models.ForeignKey(List, on_delete= models.CASCADE)
  value = models.CharField(blank = True, null = True, max_length= 40)

  def __str__(self):
    return self.value
