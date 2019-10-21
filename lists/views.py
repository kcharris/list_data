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
  fields = ["name"]

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
    users = item_list.users.all()
    def get_tag_columns(tags, items):
      """
      returns a list of organized lists that depend on the order of the objects within the tags and items variables
      """
      tag_columns = []
      count = -1
      for tag in tags:
        count += 1
        tag_columns.append([tag])
        for item in items:
          tag_columns[count].append(ItemTagValue.objects.get(tag = tag, item = item))
      return tag_columns
    tag_columns = get_tag_columns(tags, items)
    
    return render(request, "lists/list_detail.html", {'item_list': item_list, 'items':items, "tag_columns": tag_columns, 'users': users})

class ItemAddView(View):
  def get(self, request, **kwargs):

    return render(request, "lists/item_add.html")

  def post(self, request, **kwargs):
    pk = kwargs['pk']
    new_item = Item.objects.create(name = request.POST['new_item'])
    item_list = List.objects.get(pk = pk)
    item_list.items.add(new_item)
    for tag in item_list.tags.all():
      item_list.tag_values.add(ItemTagValue.objects.create(item = new_item, tag = tag))

    return HttpResponseRedirect(reverse('list-detail', args=[kwargs['pk']]))

class ItemUpdateView(View):
  def get(self, request, **kwargs):
    item = Item.objects.get(pk = kwargs['pk2'])
    tag_values = ItemTagValue.objects.filter(item = item)
    
    return render(request, 'lists/item_update.html', { "item": item, "tag_values": tag_values, 'list_pk': kwargs['pk'] })

  def post(self, request, **kwargs):
    item = Item.objects.get(pk = kwargs["pk2"])
    for x in request.POST:
      if len(Tag.objects.filter(name = x)) > 0:
        if len(ItemTagValue.objects.filter(tag__name = x, item = item)) > 0:
          tag_value = ItemTagValue.objects.get(tag__name = x, item = item)
          tag_value.value = request.POST[x]
          tag_value.save()
    return HttpResponseRedirect(reverse('item-update', args=[kwargs['pk'], kwargs['pk2']]))

class ItemDeleteView(View):
  def get(self, request, **kwargs):

    Item.objects.get(pk = kwargs['pk2']).delete()
    return HttpResponseRedirect(reverse('list-detail', args=[kwargs['pk']]))

class TagAddView(View):
  def get(self, request, **kwargs):

    return render(request, 'lists/tag_add.html')

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
        if len(ItemTagValue.objects.filter(tag = tag, item = item)) < 1:
          ITV = ItemTagValue.objects.create(tag = tag, item = item)
          ITV.lists.add(item_list)
    return HttpResponseRedirect(reverse("list-detail", args= [kwargs['pk']]))      

class TagUpdateView(View):
  def get(self, request, **kwargs):
    item_list = List.objects.get(pk = kwargs['pk'])

    return render(request, 'lists/tag_update.html', {'item_list': item_list})
  def post(self, request, **kwargs):
    item_list = List.objects.get(pk = kwargs['pk'])
    for x in request.POST:
      if len(Tag.objects.filter(name = x)) > 0:
        tag = Tag.objects.get(name = x)
        if tag.name != request.POST[x]:
          item_list.tags.remove(tag)
          if len(Tag.objects.filter(name = request.POST[x])) == 0:
            new_tag = Tag.objects.create(name = request.POST[x])
            for item in item_list.items.all():
              if len(ItemTagValue.objects.filter(tag = new_tag, item = item)) < 1:
                ITV = ItemTagValue.objects.create(tag = new_tag, item = item)
                ITV.lists.add(item_list)
            item_list.tags.add(Tag.objects.get(name = request.POST[x]))
    return HttpResponseRedirect(reverse('tag-update', args=[kwargs['pk']]))
class TagRemoveView(View):
  def get(self, request, **kwargs):
    item_list = List.objects.get(pk = kwargs['pk'])
    tag = Tag.objects.get(name = kwargs['tag'])
    item_list.tags.remove(tag)
    return HttpResponseRedirect(reverse('tag-update', args= [kwargs['pk']]))

