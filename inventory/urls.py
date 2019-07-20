from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.index, name= 'index'),
  path("item_list/", views.item_list),
  path('confirmation/', views.confirmation),
  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/", views.account.as_view()),
  path("accounts/create/", views.CreateAccount.as_view(), name = "create"),
  path("users/", views.UserList.as_view(), name = "users"),
]