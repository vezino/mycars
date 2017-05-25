from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views
from reports.views import Dashbord, DriversTripReport, DriversPaymentReport

urlpatterns = [
    url(r'^$', login_required(Dashbord.as_view(), login_url='/login/'), name="Dashbord"),
    url(r'^driver/$', login_required(DriversTripReport.as_view(), login_url='/login/'), name="DriversTripReport"),
    url(r'^payment/$', login_required(DriversPaymentReport.as_view(), login_url='/login/'), name="DriversPaymentReport"),
    #url(r'^landing/$', views.LandingView.as_view(), name='land'),
]