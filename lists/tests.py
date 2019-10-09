from django.test import TestCase
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import ListCreateView
from .models import List

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