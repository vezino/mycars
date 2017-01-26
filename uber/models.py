# coding=utf-8
# Note: The above line define the encoding!
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
# Unicode 
import unicodedata
# Create your models here.
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
