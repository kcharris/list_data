from . import views
from django.urls import path, include


urlpatterns = [
  path('music/', views.Index.as_view(), name= 'music'),
  path("music_list/", views.ItemList.as_view(), name = "music_list"),
  path('confirmation/', views.Confirmation.as_view(), name = 'confirmation'),
  path('accounts_music_list/', views.AccountMusicList.as_view(), name = "accounts_music_list")
]