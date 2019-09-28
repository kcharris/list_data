from django.urls import path
from .views import ListsList

urlpatterns = [
    path('lists/', ListsList.as_view()),
]