from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListsListView.as_view(), name = "lists-list"),
    path('list/add/', ListCreateView.as_view(), name = 'list-add'),
    path('list/<int:pk>/update', ListUpdateView.as_view(), name = 'list-update'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name = 'list-delete'),
    path('list/<int:pk>/detail/', ListDetailView.as_view(), name = 'list-detail'),
    path('list/<int:pk>/tag/add/', TagAddView.as_view(), name = 'tag-add'),
    path('list/<int:pk>/item/add/', ItemAddView.as_view(), name = 'item-add')

]