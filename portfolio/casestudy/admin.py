from django.contrib import admin
# Register your models here.
from .models import CaseStudy, Item

admin.site.register(CaseStudy)
admin.site.register(Item)
