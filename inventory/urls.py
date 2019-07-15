from . import views
from django.urls import path

urlpatterns = [
  path('', views.index, name= 'index'),
  path("item_list/", views.item_list, name = "item_list"),
  path('confirmation/', views.confirmation, name = "confirmation")
]