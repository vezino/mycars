from django.contrib import admin

# Register your models here.
from .models import Vehicle, Brand, VehicleAssigment
admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(VehicleAssigment)