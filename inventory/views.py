from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Song, Album, Artist, SongForm, UserRating

# Create your views here.
def index(request):
  
  return render(request, "inventory/index.html")

def item_list(request):  
  if request.method == "GET":
    song_form = SongForm()
    songs = Song.objects.all()
    if request.user.is_authenticated:
      is_auth = True
      usersongs = request.user.songs.all()
    else:
      is_auth = False
      usersongs = []
    return render(request, "inventory/item_list.html", {"songs" : songs, "is_auth": is_auth, "usersongs": usersongs, "song_form": song_form})
  if request.method == "POST":
    form = request.POST
    if "delete" in form:
      for x in form.getlist("delete"):
        song = Song.objects.filter(name = x)
        song.delete()
    if "add" in form:
      for x in form.getlist("add"):
        song = Song.objects.get(name = x)
        song.users.add(request.user)
        UserRating.objects.create(user = request.user, song = song, rating = song.rating)
    return HttpResponseRedirect(reverse("item_list"))

def confirmation(request):
  song_form = SongForm(request.POST)
  song_form.save()
  return HttpResponseRedirect(reverse("item_list"))

class AccountItemList(View):
  def get(self, request):
    if request.user.is_authenticated:
      songs = Song.objects.filter(users = request.user)
      user_ratings = UserRating.objects.filter(user = request.user)
      return render(request, "inventory/account_item_list.html", {"songs": songs, "user_ratings": user_ratings})
    else:
      return HttpResponseRedirect(reverse("login"))
  def post(self, request):
    if "remove" in request.POST:
      for x in request.POST.getlist("remove"):
        song = Song.objects.get(name = x)
        song.users.remove(request.user)
        UserRating.objects.filter(user = request.user, song = song).delete()

      return HttpResponseRedirect(reverse("accounts_item_list"))

class CreateAccount(View):
  def get(self, request):
    form = UserCreationForm()
    return render(request, "registration/register.html", {"form" : form })
  def post(self, request):
    form2 = UserCreationForm(request.POST)
    if form2.is_valid():
      form2.save()
    else:
      return HttpResponseRedirect(reverse("register"))
    return HttpResponseRedirect(reverse("login"))

class UserList(View):
  def get(self, request):
    users = User.objects.all()
    return render(request, "inventory/users.html", {"users" : users})

class Account(View):
  def get(self, request):
    user = request.user
    return render(request, "inventory/accounts.html", {"user" : user})