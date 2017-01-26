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
  FUEL_TYPE = (
    ("0","Selecciona el tipo de gasolina"),
    ("Magna","Magna"),
    ("Premium","Premium"),
    ("Disel","Disel"),
    )
  vehicleassigment = models.ForeignKey(models_vehicle.VehicleAssigment,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name= "vehiculo asignado")
  odo = models.FloatField("kilometraje al momento de la carga",default=0)
  odo_picture = models.ImageField("foto de odometro",upload_to="expense/gas_odo/",default="")
  fuel_type = models.CharField("tipo de combustible",max_length=7,default= "",choices = FUEL_TYPE)
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

@python_2_unicode_compatible
class GasCardUsage(models.Model):
  FUEL_TYPE = (
    ("0","Selecciona el tipo de gasolina"),
    ("Magna","Magna"),
    ("Premium","Premium"),
    ("Disel","Disel"),
    )
  company = models.CharField(max_length=50,default= "")
  date_usage = models.DateField("fecha de carga",default=datetime.now)
  time_usage = models.TimeField("hora de carga",default=datetime.now)
  bin_number = models.CharField(max_length=20,default= "")
  owner_name = models.CharField(max_length=100,default= "")
  fuel_type = models.CharField("tipo de combustible",max_length=7,default= "",choices = FUEL_TYPE)
  station_number = models.CharField(max_length=6,default= "")
  plate = models.CharField(max_length=7,default= "")
  kms = models.FloatField("kilometraje",default=0)
  vehicle_description = models.CharField(max_length=100,default= "")
  vehicle_serial_number = models.CharField(max_length=20,default= "")
  charge_date = models.DateField("fecha de cargo",default=datetime.now)
  gas_liters = models.FloatField("litros",default=0)
  gas_price = models.FloatField("precio x litro",default=0)
  ieps = models.FloatField("ieps",default=0)
  initial_balance = models.FloatField("balance inicial",default=0)
  final_balance = models.FloatField("balance final",default=0)
  gas_total_without_tax = models.FloatField("total",default=0)
  commission_without_tax = models.FloatField("comision sin iva",default=0)
  comission_tax = models.FloatField("iva comision",default=0)
  rendimiento = models.FloatField("rendimiento",default=0)
  id_tx = models.IntegerField("id tx",default=0)
  card_status = models.CharField("status de la tarjeta",max_length=20,default= "")
  period = models.CharField("periodo",max_length=20,default= "")
  invoice_folio = models.CharField("folio factura",max_length=20,default= "")
  folio_tx = models.CharField("folio tx",max_length=20,default= "")
  class Meta:
    verbose_name_plural = "Tarjeta gastos gasolina"
  def __str__(self):
    return self.folio_tx + " " +str(self.date_usage) + "(" + self.plate + ")" 





