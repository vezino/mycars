from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. We are in development please go to admin to add catalog information.")

class LandingView(View):
  template_name = 'site_base.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name)



