from django.test import TestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import ListCreateView
from .models import *

# Create your tests here.

class ListCreateViewTests(TestCase):
  def setUp(self):
    User.objects.create_user(username ='testuser', password= 'password')
  def test_user_create_list(self):
    """
    tests whenever a list is created it is connected to the user that created it
    """
    c = Client()
    c.login(username= 'testuser', password = 'password')
    c.post('/inventory/list/add/', {'name': 'testname'})

    self.assertEqual(List.objects.get(name = 'testname'), List.objects.get(users__username = 'testuser'))

class ItemUpdateViewTests(TestCase):
  def setUp(self):
    User.objects.create_user(username ='testuser', password= 'password')
    item = Item.objects.create(name = 'item')
    tag = Tag.objects.create(name = 'tag')
    tag_value = ItemTagValue.objects.create(value = 'one', tag = tag, item = item)
    list1 = List.objects.create(name = 'list')
    list1.tags.add(tag)
    list1.items.add(item)
    list1.tag_values.add(tag_value)

  def test_sending_to_post(self):
    c = Client()

    list1 = List.objects.get(name = 'list')
    item = Item.objects.get(list = list1)

    response = c.post("inventory/list/{}/item/update/{}".format(list1.pk, item.pk), {'tag': 'new'})
    
    self.assertGreater(len(List.objects.filter(tag_values__value = 'two')), 0)

