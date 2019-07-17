from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import *

from .models import Song, Album, Artist, SongForm

# Create your views here.
def index(request):
  song_form = SongForm()
  return render(request, "inventory/index.html", {'song_form' : song_form})

def item_list(request):  
  songs = Song.objects.all()
  return render(request, "inventory/item_list.html", {"songs" : songs})

def confirmation(request):
  form = SongForm(request.POST)
  new_song = form.save()
  return HttpResponseRedirect('../')

#def accounts(request):
