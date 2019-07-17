from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.index, name= 'index'),
  path("item_list/", views.item_list),
  path('confirmation/', views.confirmation),
  path('accounts/', include('django.contrib.auth.urls'))
]