from django.shortcuts import render
from .models import Idea, Category
from django.views.generic import ListView, DetailView
# Create your views here.
class IdeaListView(ListView):
    model = Idea

class SecretView(TemplateView):
    template_name="kaizen/secrets.html"
