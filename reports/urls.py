from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^landing/$', views.LandingView.as_view(), name='land'),
]