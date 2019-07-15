from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Song, Album, Artist

# Create your views here.
def index(request):
  return render(request, "inventory/index.html")

def item_list(request):  
  songs = Song.objects.all()
  return render(request, "inventory/item_list.html", {"songs" : songs})

def confirmation(request):
  form = request.POST
  b = Song.objects.create(name = form['song'])
  b.save()
  return HttpResponseRedirect('../')