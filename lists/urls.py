from django.urls import path
from .views import InventoryView, ListsList, ListCreate, ListUpdate, ListDelete

urlpatterns = [
    path('', InventoryView.as_view(), name = 'inventory'),
    path('lists/', ListsList.as_view(), name = "lists-list"),
    path('list/add/', ListCreate.as_view(), name = 'list-add'),
    path('list/<int:pk>/', ListUpdate.as_view(), name = 'list-update'),
    path('list/<int:pk>/delete/', ListDelete.as_view(), name = 'list-delete'),
]