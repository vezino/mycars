from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse
#from django.views import View
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView

@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Hello, world. We are in development please go to admin to add catalog information.")

#@login_required(login_url="/login/")
class LandingView(View):
  template_name = 'site_base.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name)



