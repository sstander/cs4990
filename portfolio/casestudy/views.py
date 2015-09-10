from django.shortcuts import render
from django.views import generic

from .models import CaseStudy, Item

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'casestudy/index.html'
    model = CaseStudy

class DetailView(generic.DetailView):
    template_name = 'casestudy/detail.html'
    model = CaseStudy
