from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', login_required(views.ClockInOutView.as_view()), name="ko"),
    url(r'^punches/(?P<pk>\d+)/$', login_required(views.PunchListView.as_view()), name="punches"),
]
