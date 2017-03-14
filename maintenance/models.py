from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# Unicode 
import unicodedata

# Validation error stuff
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

#External model reference
from vehicle import models as models_vehicle
# Create your models here.

@python_2_unicode_compatible
class ServiceConcept(models.Model):
  name = models.CharField("concepto",max_length=50,unique=True)
  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "concepto del servicio"
    ordering = ['name']
  def __str__(self):
    return self.name

@python_2_unicode_compatible
class ServiceItem(models.Model):
  concept = models.ForeignKey('ServiceConcept',
    on_delete=models.CASCADE,
    related_name='ServiceItem',
    verbose_name= "concepto")
  name = models.CharField("descripcion",max_length=100)
  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "descripcion del trabajo"
    ordering = ['concept','name']
  def __str__(self):
    return self.concept.name + ' ( ' + self.name + ' )'

@python_2_unicode_compatible
class ServiceItemPrice(models.Model):
  service_item = models.ForeignKey('ServiceItem',
    on_delete=models.CASCADE,
    related_name='ServiceItemPrice',
    verbose_name= "Trabajo")
  #spare_parts = models.FloatField("precio refacciones",default=0)
  #workforce = models.FloatField("mano de obra",default=0)
  class Meta:
    verbose_name_plural = "importe del trabajo"
  def __str__(self):
    #return str(self.service_item) + ' [Refacciones: ($ ' + str(self.spare_parts) + ')' + ' ]'
    return str(self.service_item)


@python_2_unicode_compatible
class ServiceOrder(models.Model):
  vehicle = models.ForeignKey(models_vehicle.Vehicle,on_delete=models.CASCADE,verbose_name="vehiculo")
  # Service dates
  date = models.DateTimeField("fecha de elaboracion",default=datetime.now)
  reception = models.DateTimeField("fecha de entrada del vehiculo",default=datetime.now,blank=True)
  delivery = models.DateTimeField("fecha de entrega del vehiculo",default=datetime.now,blank=True)
  # Inventory
  radio = models.NullBooleanField("radio")
  floor_mats = models.NullBooleanField("tapetes")
  lighter = models.NullBooleanField("eencendedor")
  extinguisher = models.NullBooleanField("extinguidor")
  hydraulic_jack = models.NullBooleanField("gato")
  tools = models.NullBooleanField("herramientas")
  wheel_brace = models.NullBooleanField("llave de cruz")
  spare_tire = models.NullBooleanField("llanta de refaccion")
  oil_cap = models.NullBooleanField("tapon de aceite")
  radiator_cap = models.NullBooleanField("tapon de radiador")
  dipstick = models.NullBooleanField("varilla de aceite")
  antenna = models.NullBooleanField("antena")
  mirrors = models.NullBooleanField("espejos")
  crystals = models.NullBooleanField("cristales")
  wheel_covers = models.NullBooleanField("tapones")
  gas_cap = models.NullBooleanField("tapon de gasolina")
  comments = models.TextField("observaciones",default="",blank=True)
  total_amount = models.FloatField("total de la reparacion",default=0)
  tax_amount =  models.FloatField("iva",default=0)
  total_final = models.FloatField("total con iva",default=0)
  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)

  class Meta:
    verbose_name_plural = "orden de servicio"
    #ordering = ['concept','name']
  def __str__(self):
    return self.vehicle.model_name


class ServiceOrderTotal(models.Model):
  service_order_detail = models.ForeignKey(ServiceOrder, on_delete=models.CASCADE,verbose_name="Orden de Servicio")
  #ServiceItemPrice
  service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE,verbose_name="Descripcion del trabajo")
  spare_parts = models.FloatField("precio refacciones",default=0)
  workforce = models.FloatField("mano de obra",default=0)
  item_total = models.FloatField("total",default=0)


  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)


  class Meta:
    verbose_name_plural = "Trabajos Realizados"



