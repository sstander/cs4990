from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Item, Category

# Create your views here.
class CategoryListView(ListView):
    model = Category

class CreateCategoryView(CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('catalog:categorylist')

class UpdateCategoryView(UpdateView):
    model = Category
    fields = ['name', 'description']

class DeleteCategoryView(DeleteView):
    model = Category

class ItemListView(ListView):
    model = Item
    #def get_.....

class CreateItemView(CreateView):
    model = Item
    fields = ['name', 'quantity', 'sku', 'category']
    success_url = reverse_lazy('catalog:itemlist')

class UpdateItemView(UpdateView):
    model = Item
    fields = ['name', 'quantity', 'sku', 'category']

class DeleteItemView(DeleteView):
    model = Item
