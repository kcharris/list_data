from . import views
from django.urls import path, include


urlpatterns = [
  path('', views.Index.as_view(), name= 'index'),
  path("item_list/", views.ItemList.as_view(), name = "item_list"),
  path('confirmation/', views.Confirmation.as_view(), name = 'confirmation'),
  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/", views.Account.as_view(), name = 'accounts'),
  path('accounts/item_list/', views.AccountItemList.as_view(), name = "accounts_item_list"),
  path("accounts/register/", views.CreateAccount.as_view(), name = "register"),
  path("users/", views.UserList.as_view(), name = "users"),
]