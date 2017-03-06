from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views
from reports.views import Dashbord

urlpatterns = [
    url(r'^$', login_required(Dashbord.as_view(), login_url='/login/'), name="Dashbord"),
    #url(r'^landing/$', views.LandingView.as_view(), name='land'),
]