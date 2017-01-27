from django.contrib import admin

# Register your models here.
from .models import ServiceConcept,ServiceItem,ServiceItemPrice,ServiceOrder,ServiceOrderTotal

# class ServiceItemPriceInLine(admin.StackedInline):
#   model = ServiceItemPrice
#   extra = 2
class PriceInline(admin.StackedInline):
    model = ServiceOrderTotal
    extra = 0

class ServiceOrderAdmin(admin.ModelAdmin):
  fieldsets = [
  (None,               {'fields': ['vehicle','date','reception','delivery']}),
  ('Inventario',       {'fields': ['radio','floor_mats','lighter','extinguisher','hydraulic_jack','tools','wheel_brace','spare_tire','oil_cap','radiator_cap','dipstick','antenna','mirrors','crystals','wheel_covers','gas_cap'], 'classes': ['collapse']}),
  ]
  inlines = [PriceInline]


admin.site.register(ServiceOrder,ServiceOrderAdmin)
admin.site.register(ServiceConcept)
admin.site.register(ServiceItem)  
admin.site.register(ServiceItemPrice)  
