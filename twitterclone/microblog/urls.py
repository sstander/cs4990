
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.ListAllPosts.as_view(), name="allposts"),
    url(r'^myfeed/$', login_required(views.MyFeedView.as_view()), name="myfeed"),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name="profiledetail"),
    #url(r'^profile/(?P<pk>\d+)/edit/$', login_required(views.ProfileFormView.as_view()), name="editprofile"),
    url(r'^profile/(?P<pk>\d+)/follow/$', login_required(views.FollowFormView.as_view()), name="follow"),
    url(r'^profile/(?P<pk>\d+)/follow/success/$', login_required(views.FollowSuccessView.as_view()), name="followsuccess"),
    url(r'^newpost/$', views.NewPostView.as_view(), name="addpost"),
]
