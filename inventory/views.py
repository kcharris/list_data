from django.shortcuts import render
from django.http import HttpResponse

from .models import Song, Album, Artist

# Create your views here.
def index(request):
  songs = Song.objects.all()
  return render(request, inventory/index.html, {songs : songs})