from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import List

# Create your views here.

class InventoryView(View):
  def get(self, request):
    return render(request, 'lists/inventory.html')

class ListsListView(ListView):
  model = List

class ListCreateView(CreateView):
  model = List
  fields = ["name"]

  success_url = reverse_lazy('inventory')

class ListUpdateView(UpdateView):
  model = List
  fields = ["name"]

  success_url = reverse_lazy("inventory")

class ListDeleteView(DeleteView):
  model = List
  success_url = reverse_lazy('inventory')

class ListDetailView(DetailView):
  model = List

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

