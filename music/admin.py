from django.contrib import admin
from .models import Song, Artist, Album

# Register your models here.
@admin.register(Song, Album, Artist)
class MusicAdmin(admin.ModelAdmin):
  pass