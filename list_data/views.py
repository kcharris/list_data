from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

class ListData(View):
  def get(self, request):

    return render(request, "list_data/index.html")

class Account(View):
  def get(self, request):
    user = request.user
    if not user.is_authenticated:
      return HttpResponseRedirect(reverse("login"))
    return render(request, "list_data/accounts.html", {"user" : user})

class UserList(View):
  def get(self, request):
    users = User.objects.all()
    return render(request, "list_data/users.html", {"users" : users})

class CreateAccount(View):
  def get(self, request):
    form = UserCreationForm()
    return render(request, "registration/register.html", {"form" : form })
  def post(self, request):
    form2 = UserCreationForm(request.POST)
    if form2.is_valid():
      form2.save()
    else:
      return HttpResponseRedirect(reverse("register"))
    return HttpResponseRedirect(reverse("login"))

