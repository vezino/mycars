from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views
#from reports.views import Dashbord
from uber.views import UploadUberDataListView, UploadUberDataCreateView

urlpatterns = [
    url(r'^list/$', login_required(UploadUberDataListView.as_view(), login_url='/login/'), name="UploadUberData"),
	url(r'^$', login_required(UploadUberDataCreateView.as_view(), login_url='/login/'), name="UploadUberDataCreate"),
    #url(r'^landing/$', views.LandingView.as_view(), name='land'),
]