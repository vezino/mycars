from django.contrib import admin

# Register your models here.
from .models import Vehicle,Brand
admin.site.register(Brand)
admin.site.register(Vehicle)