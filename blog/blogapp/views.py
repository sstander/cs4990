from django.shortcuts import render
from django.views import generic

from .models import Post, Comment, Category

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blogapp/index.html'
    model = Post

class DetailView(generic.DetailView):
    template_name = 'blogapp/detail.html'
    model = Post
