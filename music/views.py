from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Song, Album, Artist, SongForm, UserRating

# Create your views here.
class Music(View):
  def get(self, request):
  
    return render(request, "music/music.html")

class Songs(View):  
  def get(self, request):
    song_form = SongForm()
    search_form = request.GET
    if 'q' in search_form:
      songs = (Song.objects.filter(name__startswith= search_form['q'])).order_by('name')
    else:
      songs = Song.objects.all().order_by("name")
    
    if request.user.is_authenticated:
      is_auth = True
      usersongs = request.user.songs.all()
    else:
      is_auth = False
      usersongs = []
    return render(request, "music/music_list.html", {"songs" : songs, "is_auth": is_auth, "usersongs": usersongs, "song_form": song_form})
  def post(self, request):
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
    return HttpResponseRedirect(reverse("music_list"))

class Confirmation(View):
  def post(self, request):
    song_form = SongForm(request.POST)
    song_form.save()
    return HttpResponseRedirect(reverse("music_list"))

class AccountMusicList(View):
  def get(self, request):
    if request.user.is_authenticated:
      songs = Song.objects.filter(users = request.user)
      user_ratings = UserRating.objects.filter(user = request.user)
      return render(request, "music/account_music_list.html", {"songs": songs, "user_ratings": user_ratings})
    else:
      return HttpResponseRedirect(reverse("login"))
  def post(self, request):
    if "new_rating" in request.POST:
      rating = request.POST.getlist("new_rating")
      user_songs = request.POST.getlist('user_songs')
      for x in range(len(rating)):
        if rating[x] == "":
          continue
        user_rating_object = UserRating.objects.get(user = request.user, song = Song.objects.get(name = user_songs[x]))
        user_rating_object.rating = rating[x]
        user_rating_object.save()
    if "priority" in request.POST:
      priority = request.POST.getlist("priority")
      user_songs = request.POST.getlist('user_songs')
      for x in range(len(priority)):
        if priority[x] == "":
          continue
        user_rating_object = UserRating.objects.get(user= request.user, song = Song.objects.get(name = user_songs[x]))
        user_rating_object.priority = priority[x]
        user_rating_object.save()

    if "remove" in request.POST:
      for x in request.POST.getlist("remove"):
        song = Song.objects.get(name = x)
        song.users.remove(request.user)
        UserRating.objects.filter(user = request.user, song = song).delete()

    return HttpResponseRedirect(reverse("accounts_music_list"))


