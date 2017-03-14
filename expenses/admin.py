from django.contrib import admin

# Register your models here.
class GasexpenseAdmin(admin.ModelAdmin):
  list_display = ('date_load','vehicleassigment')

from .models import Gasexpense
admin.site.register(Gasexpense,GasexpenseAdmin)