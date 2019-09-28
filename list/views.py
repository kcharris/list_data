from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
class ListsList(ListView):
  model = List

class ListCreate(CreateView):
  model = List
  fields = ["name"]

class ListUpdate(UpdateView):
  model = List
  fields = ["name"]

class ListDelete(DeleteView):
  model = List
  fields = ["name"]