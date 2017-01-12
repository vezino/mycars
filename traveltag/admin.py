from django.contrib import admin

# Register your models here.
from .models import Tagcompany,Tagcard
admin.site.register(Tagcompany)
admin.site.register(Tagcard)