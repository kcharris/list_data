from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(List, Tag, Item, ItemTagValue)
class ListAdmin(admin.ModelAdmin):
  pass