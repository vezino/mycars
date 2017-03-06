"""mycars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# Allauth views
#from allauth.account import views as allauthviews
#from django.contrib.auth import views as auth_views

# static files
from django.conf import settings
from django.conf.urls.static import static
# Login sutuff
from loginu.forms import LoginForm
from django.contrib.auth import views

#import allauth

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('loginu.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^insurances/', include('insurances.urls')),
    url(r'^reports/', include('reports.urls')),
    #url(r'^', include('insurances.urls')),
    #url(r'^accounts/', include('allauth.urls')),
    #url('^', include('django.contrib.auth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
