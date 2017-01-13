# coding=utf-8
# Note: The above line define the encoding!

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
from drivers import models as models_drivers
# Unicode 
import unicodedata

# Create your models here.
class Brand(models.Model):
  name = name = models.CharField("marca",max_length=100)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Marcas"

  def __str__(self):
    return self.name

class Vehicle(models.Model):
  MODEL_YEAR = (
    ("2006","2006"),
    ("2007","2007"),
    ("2008","2008"),
    ("2009","2009"),
    ("2010","2010"),
    ("2011","2011"),
    ("2012","2012"),
    ("2013","2013"),
    ("2014","2014"),
    ("2015","2015"),
    ("2016","2016"),
    ("2017","2017"),
    ("2018","2018"),
    ("2019","2019"),
    ("2020","2020"),
    ("2021","2021"),
    ("2022","2022"),
    ("2023","2023"),
    ("2024","2024"),
    ("2025","2025"),
    ("2026","2026"),
    )
  FUEL_TYPE = (
    ("0","Selecciona el tipo de gasolina"),
    ("Magna","Magna"),
    ("Premium","Premium"),
    ("Disel","Disel"),
    )
  brand = models.ForeignKey('Brand',
    on_delete=models.CASCADE,
    related_name='brand',
    verbose_name= "marca")
  policy =  models.ForeignKey('insurances.Policy',
    on_delete=models.CASCADE,
    related_name='policy',
    verbose_name= "poliza")
  model_name = models.CharField("modelo",max_length=20)
  make_year = models.CharField("año de fabricacion",max_length=4,default= 0,choices = MODEL_YEAR)
  plate = models.CharField("placa",max_length=10,unique=True)
  serial_number = models.CharField("numero de serie",max_length=30,unique=True,default=0)
  passengers = models.IntegerField('pasajeros',default=4)
  color = models.CharField("color",max_length=20)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  cylinders = models.IntegerField('cilindros',default=4)
  fuel_type = models.CharField("tipo de combustible",max_length=7,default= 0,choices = FUEL_TYPE)
  class Meta:
    verbose_name_plural = "Vehiculos"
  def __str__(self):
    return self.brand.name + " " +self.model_name + "(" + self.plate + ")" 

class VehicleAssigment(models.Model):
  vehicle = models.ForeignKey(Vehicle,
    on_delete=models.CASCADE,
    related_name="Vehicle",
    verbose_name= "vehiculo")
  driver = models.ForeignKey(models_drivers.Driver,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name="chofer")
  start_at = models.DateTimeField("inicio de la asignacion",default=datetime.now)
  initial_odo = models.FloatField("kilometraje inicial",default=0)
  end_at = models.DateTimeField("fin de la asignacion",default=datetime.now)
  final_odo = models.FloatField("kilometraje final",default=0)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Asignaciones de Vehiculo"
  def __str__(self):
    return self.vehicle.model_name + "( "+ self.vehicle.plate + ") - " + self.driver.name + " " +self.driver.last_name + " " + str(self.start_at)
  
