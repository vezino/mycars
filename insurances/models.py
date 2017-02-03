# coding=utf-8
# Note: The above line define the encoding!

from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Unicode shite
import unicodedata

# Validation error stuff
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.

@python_2_unicode_compatible
class Company(models.Model):
  name = models.CharField("compañia",max_length=100)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Compañias"

  def __str__(self):
    return self.name

@python_2_unicode_compatible
class Policy(models.Model):
  COVER_TYPE = (('0','N/A'),('Amplia','Amplia'),('Limitada','Limitada'),('Daños a terceros','Daños a terceros')
    )
  company = models.ForeignKey('Company',
    on_delete=models.CASCADE,
    related_name='company',
    verbose_name= "compañia aseguradora")
  reference = models.CharField("numero de poliza",max_length=30)
  start_at = models.DateTimeField("inicio de vigencia",default=datetime.now)
  end_at = models.DateTimeField("fin vigencia",default=datetime.now)
  price = models.FloatField("costo del seguro",default=0,help_text="costo el seguro")
  image = models.ImageField("foto poliza:",upload_to="insurances/",default="")
  # cover data
  cover_damage = models.CharField("cobertura daños materiales",max_length=250,default="")
  cover_robbery = models.CharField("cobertura robo",max_length=250,default="")
  cover_medic_expense = models.CharField("cobertura medica",max_length=250,default="")
  cover_total = models.CharField("cobertura total",max_length=250,default="")
  # Cover Type
  cover_type = models.CharField("tipo de cobertura",max_length=20,default= 0,choices = COVER_TYPE)
  # Change Control
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  phone = models.CharField("numero de la aseguradora",max_length=10,default="",help_text="Indica el número para llamar en caso de un sinisetro, solo numeros")
  class Meta:
    verbose_name_plural = "Polizas"

  def __str__(self):
    status =""
    if self.insurance_valid(): 
      status = "Vigente"
    else:
      status = "Vencido"
    return self.company.name + ' (' + self.reference + ')' + ' - ' + status

  # Check if Insurance is valid
  def insurance_valid(self):
    if self.end_at > datetime.now(timezone.utc):
      return True
    else:
      return False

  #Validate end_at to be greater then start_at on submit data
  def clean(self, *args, **kwargs):
    if self.end_at < self.start_at:
      raise ValidationError(_('Fin de vigencia debe ser mayor que Inicio de vigencia!'),code='invalid')
    super(Policy, self).save(*args, **kwargs)







