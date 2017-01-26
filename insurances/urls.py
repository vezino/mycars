from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views
from insurances.views import LandingView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/$', login_required(LandingView.as_view(), login_url='/login/'), name="Landing"),
]