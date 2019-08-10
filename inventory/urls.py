from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.index, name= 'index'),
  path("item_list/", views.item_list, name = "item_list"),
  path('confirmation/', views.confirmation, name = 'confirmation'),
  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/", views.Account.as_view(), name = 'accounts'),
  path('accounts/item_list/', views.AccountItemList.as_view(), name = "accounts_item_list"),
  path("accounts/register/", views.CreateAccount.as_view(), name = "register"),
  path("users/", views.UserList.as_view(), name = "users"),
]