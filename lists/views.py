from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import List, Item, Tag, ItemTagValue

# Create your views here.

class ListsListView(ListView):
  model = List

class ListCreateView(CreateView):
  model = List
  fields = ["name", "tags"]

  def form_valid(self, form):
    self.object = form.save()
    self.object.users.add(self.request.user)
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())

class ListUpdateView(UpdateView):
  model = List
  fields = ["name", "tags", "items"]

  success_url = reverse_lazy("lists-list")

class ListDeleteView(DeleteView):
  model = List
  success_url = reverse_lazy('lists-list')

class ListDetailView(View):
  def get(self, request, **kwargs):
    pk = kwargs['pk']
    item_list = List.objects.get( pk = pk )
    items = Item.objects.filter( list = item_list )
    tags = Tag.objects.filter( list = item_list)
    tag_values = ItemTagValue.objects.filter(list = item_list)
    users = item_list.users.all()
    
    return render(request, "lists/list_detail.html", {'item_list': item_list, 'items':items, 'tags': tags, 'tag_values': tag_values, 'users': users})

class TagAddView(View):
  def get(self, request, **kwargs):
    item_list = List.objects.get(pk = kwargs['pk'])

    return render(request, 'lists/tag_add.html', {'item_list': item_list })

  def post(self, request, **kwargs):
    name = request.POST['name']
    item_list = List.objects.get(pk = kwargs['pk'])
    if len(Tag.objects.filter(name = name)) == 0:
      Tag.objects.create(name = name)
    tag = Tag.objects.get(name = name)
    if tag not in item_list.tags.all():
      item_list.tags.add(tag)
    if len(item_list.items.all()) > 0:
      for item in item_list.items.all():
        ITV = ItemTagValue.objects.create(tag = tag, item = item)
        ITV.lists.add(item_list)
    return HttpResponseRedirect(reverse("list-detail", args= [kwargs['pk']]))      


  

