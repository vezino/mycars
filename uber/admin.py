from django.contrib import admin

from .models import UberData, UploadUberData
# Register your models here.

class UploadUberDataAdmin(admin.ModelAdmin):
	list_display = ('created_at','name','uber_file_uploaded')

admin.site.register(UberData)
admin.site.register(UploadUberData,UploadUberDataAdmin)