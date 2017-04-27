# coding=utf-8
# Note: The above line define the encoding!

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# External model reference
from drivers import models as models_drivers
from traveltag import models as models_traveltag

# Unicode 
import unicodedata

# Validation error stuff
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
@python_2_unicode_compatible
class Brand(models.Model):
  name = models.CharField("marca",max_length=100)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Marcas"

  def __str__(self):
    return self.name

@python_2_unicode_compatible
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

@python_2_unicode_compatible
class VehicleAssigment(models.Model):
  # ForeignKey's
  vehicle = models.ForeignKey(Vehicle,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name= "vehiculo")
  driver = models.ForeignKey(models_drivers.Driver,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name="chofer")
  traveltag = models.ForeignKey(models_traveltag.Tagcard,
    on_delete=models.CASCADE,
    related_name="vehicleassigment",
    verbose_name="TAG")
  # Model fields
  start_at = models.DateTimeField("inicio de la asignacion",default=datetime.now)
  initial_odo = models.FloatField("kilometraje inicial",default=0)
  end_at = models.DateTimeField("fin de la asignacion",default=datetime.now)
  final_odo = models.FloatField("kilometraje final",default=0)
  # Date log
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Asignaciones de Vehiculo"  

  def __str__(self):
    # translate status_vehicle_assigment
    status="Terminada"
    if self.status_vehicle_assigment():
      status = "Actual"
    return self.vehicle.model_name + " ["+ self.vehicle.plate + "] - Chofrer: " + self.driver.name + " " +self.driver.last_name + " del " + str(self.start_at) + " al " + str(self.end_at) + " - Status Asignacion: " + status
  
  # Check if assigment date is active.
  def status_vehicle_assigment(self):
    if self.end_at > datetime.now(timezone.utc):
      return True
    else:
      return False  

  # Validate clean post data
  def clean(self, *args, **kwargs):
    if self.end_at < self.start_at:
      raise ValidationError(_('Fin la asignacion debe ser mayor que Inicio de la asignacion!'),code='invalid')
    super(VehicleAssigment, self).save(*args, **kwargs)



