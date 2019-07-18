from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

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

class CreateAccount(View):
  def get(self, request):
    form = UserCreationForm()
    return render(request, "registration/create.html", {"form" : form })
  def post(self, request):
    form2 = UserCreationForm(request.POST)
    if form2.is_valid():
      new_user = form2.save()
    return HttpResponseRedirect("../login")