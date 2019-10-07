from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import List, Item, Tag, ItemTagValue

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

class ListDetailView(View):
  def get(self, request, **kwargs):
    pk = kwargs['pk']
    item_list = List.objects.get( pk = pk )
    items = Item.objects.filter( list = item_list )
    tags = Tag.objects.filter( list = item_list)
    tag_values = ItemTagValue.objects.filter(inventory = item_list)
    
    return render(request, "lists/list_detail.html", {'item_list': item_list, 'items':items, 'tags': tags, 'tag_values': tag_values})

  

