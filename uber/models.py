# coding=utf-8
# Note: The above line define the encoding!
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
# Unicode 
import unicodedata
# Create your models here.

@python_2_unicode_compatible
class UberData(models.Model):
  TRIP_TYPE = (
    ("Trip","Trip"),
    ("Misc Payment","Misc Payment")
    )
  driver_name = models.CharField(max_length=200,default= "")
  phone_number = models.CharField(max_length=11,default="")
  email = models.EmailField(max_length=254,default="")
  trip_type = models.CharField(max_length=200,default= "",choices = TRIP_TYPE)
  trip_date = models.DateTimeField(default=datetime.now)
  description = models.TextField(max_length=200,default= "",blank=True)
  trip_number = models.CharField(max_length=40,default= "",primary_key=True,unique=True)
  fare = models.FloatField(default=0)
  surge = models.FloatField(default=0,blank=True)
  toll = models.FloatField(default=0,blank=True)
  misc = models.FloatField(default=0,blank=True)
  other = models.FloatField(default=0,blank=True)
  meter_rate = models.FloatField(default=0,blank=True)
  gratuity = models.FloatField(default=0,blank=True)
  commission = models.FloatField(default=0)
  tax_on_fee = models.FloatField(default=0,blank=True)
  total_payment = models.FloatField(default=0)
  class Meta:
    verbose_name_plural = "Uber Data"
    ordering = ['trip_date']

  def __str__(self):  
    return self.trip_number + " ( " + str(self.trip_date) + " )"


@python_2_unicode_compatible
class UberDataAgg(models.Model):
  TRIP_TYPE = (
  ("Trip","Trip"),
  ("Misc Payment","Misc Payment")
  )
  driver_name = models.CharField(max_length=200,default= "")
  phone_number = models.CharField(max_length=11,default="")
  email = models.EmailField(max_length=254,default="")
  trip_type = models.CharField(max_length=200,default= "",choices = TRIP_TYPE)  
  trip_date = models.DateField(default=datetime.now,primary_key=True,unique=False)
  trip_year = models.IntegerField(default=0,blank=True)
  trip_month = models.IntegerField(default=0,blank=True)
  trip_day = models.IntegerField(default=0,blank=True)
  week = models.IntegerField(default=0,blank=True)
  quarter = models.IntegerField(default=0,blank=True)
  description = models.TextField(max_length=200,default= "",blank=True)
  viajes = models.IntegerField(default=0)
  fare = models.FloatField(default=0,blank=True)
  surge = models.FloatField(default=0,blank=True)
  toll = models.FloatField(default=0,blank=True)
  misc = models.FloatField(default=0,blank=True)
  other = models.FloatField(default=0,blank=True)
  meter_rate = models.FloatField(default=0,blank=True)
  gratuity = models.FloatField(default=0,blank=True)
  commission = models.FloatField(default=0,blank=True)
  tax_on_fee = models.FloatField(default=0,blank=True)
  total_payment = models.FloatField(default=0,blank=True)
  class Meta:
    verbose_name_plural = "Aggregated Uber Data"
    ordering = ['trip_date']
    managed = False

  def __str__(self):  
    return self.driver_name + " ( " + str(self.trip_date) + " )"


@python_2_unicode_compatible
class VMycarsIncomeByYearMonth(models.Model):
  trip_year = models.IntegerField(default=0,primary_key=True,unique=False)
  trip_month = models.CharField(max_length=10,default=0)
  viajes = models.IntegerField(default=0)
  total_payment = models.FloatField(default=0)
  class Meta:
    verbose_name_plural = "Year Month Uber Data"
    ordering = ['trip_year']
    db_table = 'vmycarsincomebyyearmonth'
    managed = False

  def __str__(self):  
    return str(self.trip_year) + " ( " + str(self.trip_month) + " )"  


class UploadUberData(models.Model):
  name = models.CharField("nombre de la carga",max_length=100,unique=True)
  file_procesed = models.NullBooleanField("Procesado",default=False)
  uber_file_uploaded = models.FileField("archivo de datos de uber",max_length=100,upload_to="uber/uberfiles",default="")
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Uber Data Load"
    ordering = ['created_at']


  def __str__(self):  
    return self.name







