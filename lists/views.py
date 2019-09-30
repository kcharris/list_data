from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import List

# Create your views here.

class InventoryView(View):
  def get(self, request):
    return render(request, 'lists/inventory.html')

class ListsList(ListView):
  model = List

class ListCreate(CreateView):
  model = List
  fields = ["name"]

  success_url = reverse_lazy('inventory')

class ListUpdate(UpdateView):
  model = List
  fields = ["name"]

  success_url = reverse_lazy("inventory")

class ListDelete(DeleteView):
  model = List
  success_url = reverse_lazy('inventory')