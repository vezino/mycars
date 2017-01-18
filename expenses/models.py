# coding=utf-8
# Note: The above line define the encoding!
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
from vehicle import models as models_vehicle

# Create your models here.
@python_2_unicode_compatible
class Gasexpense(models.Model):
  vehicleassigment = models.ForeignKey(models_vehicle.VehicleAssigment,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name= "vehiculo asignado")
  odo = models.FloatField("kilometraje al momento de la carga",default=0)
  odo_picture = models.ImageField("foto de odometro",upload_to="expense/gas_odo/",default="")
  gas_price = models.FloatField("precio x litro",default=0)
  gas_liters = models.FloatField("litros cargados",default=0)
  gas_total = models.FloatField("importe en pesos",default=0)
  ticket_picture = models.ImageField("foto del ticket",upload_to="expense/gas_ticket/",default="",blank=True)
  date_load = models.DateTimeField("fecha de carga",default=datetime.now)
  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "gastos de gasolina"
    ordering = ['date_load','vehicleassigment']

  def __str__(self):
    return str(self.date_load) + " - Asignacion: (" +  str(self.vehicleassigment) + ")" 
