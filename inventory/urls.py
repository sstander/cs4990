from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.CategoryListView.as_view(), name="categorylist"),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.ItemListView.as_view(), name="itemlist"),
    url(r'^category/add/$', views.CreateCategoryView.as_view(), name="addcategory"),
    url(r'^category/(?P<pk>[0-9]+)/$', views.UpdateCategoryView.as_view(), name="categoryupdate"),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.DeleteCategoryView.as_view(), name=
