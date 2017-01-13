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
class Paymentcard(models.Model):
  TYPE  = (
    ("Tarjeta de Gasolina","Tarjeta de Gasolina"),
    ("Tarjeta de Credito","Tarjeta de Credito"),
    )
  name = models.CharField("nombre",max_length=20)
  card_type =  models.CharField("tipo de tarjeta",max_length=20,default= "",choices = TYPE)
  card_number = models.CharField("numero de tarjeta",max_length=20,default=0,unique=True)
  card_limit = models.FloatField("limite de credito",default=0)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Tarjeta de Gastos"
  def __str__(self):
    return self.card_type + " - " + self.name + " - ( " + self.card_number + " )"