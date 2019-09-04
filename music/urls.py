from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.Music.as_view(), name= 'music'),
  path("list/", views.Songs.as_view(), name = "music_list"),
  path('confirmation/', views.Confirmation.as_view(), name = 'confirmation'),
  path('accounts_list/', views.AccountMusicList.as_view(), name = "accounts_music_list")
]