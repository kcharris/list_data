from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Song, Album, Artist, SongForm

# Create your views here.
def index(request):
  song_form = SongForm()
  return render(request, "inventory/index.html", {'song_form' : song_form})

def item_list(request):  
  if request.method == "GET":
    songs = Song.objects.all()
    return render(request, "inventory/item_list.html", {"songs" : songs})
  if request.method == "POST":
    form = request.POST
    for x in form:
      song = Song.objects.filter(name = x)
      song.delete()
    return HttpResponseRedirect(reverse(item_list))

def confirmation(request):
  song_form = SongForm(request.POST)
  song_form.save()
  return HttpResponseRedirect('../')

class CreateAccount(View):
  def get(self, request):
    form = UserCreationForm()
    return render(request, "registration/create.html", {"form" : form })
  def post(self, request):
    form2 = UserCreationForm(request.POST)
    if form2.is_valid():
      form2.save()
    else:
      return HttpResponseRedirect(reverse("create"))
    return HttpResponseRedirect(reverse("login"))

class UserList(View):
  def get(self, request):
    users = User.objects.all()
    return render(request, "inventory/users.html", {"users" : users})

class account(View):
  def get(self, request):
    user = request.user.username
    return render(request, "inventory/accounts.html", {"user" : user})