# coding=utf-8
# Note: The above line define the encoding!

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible
# Unicode shite
import unicodedata

# Create your models here.
@python_2_unicode_compatible
class Company(models.Model):
  name = models.CharField("compañia",max_length=100)
  created_at = models.DateTimeField("fecha de alta",default=datetime.now)
  class Meta:
    verbose_name_plural = "Compañias"

  def __str__(self):
    return self.name

@python_2_unicode_compatible
class Policy(models.Model):
  COVER_TYPE = (('0','N/A'),('1','Amplia'),('2','Limitada'),('3','Daños a terceros')
    )
  company = models.ForeignKey('Company',
    on_delete=models.CASCADE,
    related_name='company',
    verbose_name= "compañia aseguradora")
  reference = models.CharField("numero de poliza",max_length=30)
  start_at = models.DateTimeField("inicio de vigencia",default=datetime.now)
  end_at = models.DateTimeField("fin vigencia",default=datetime.now)
  price = models.FloatField("importe del seguro",default=0,help_text="cuanto costo el seguro")
  cover_amount = models.FloatField("importe de la coberura",default=0)
  cover_type = models.CharField("tipo de cobertura",max_length=1,default= 0,choices = COVER_TYPE)
  created_at = models.DateTimeField("fecha de alta",default=datetime.now)
  phone = models.CharField("numero de la aseguradora",max_length=50,default="",help_text="Indica el número para llamar en caso de un sinisetro")
  class Meta:
    verbose_name_plural = "Polizas"

  def __str__(self):
    return self.company.name + ' (' + self.reference + ')'

