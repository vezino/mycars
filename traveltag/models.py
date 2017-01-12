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
class Tagcompany(models.Model):
  name =  models.CharField("Compañia del TAG",max_length=30)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Compañia TAG"
  def __str__(self):
    return self.name

@python_2_unicode_compatible
class Tagcard(models.Model):
  company = models.ForeignKey('Tagcompany',
    on_delete=models.CASCADE,
    related_name='Tagcompany',
    verbose_name= "Compañia del TAG")
  card_number = models.CharField("Numero de TAG",max_length=30)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "TAG"
  def __str__(self):
    return self.company.name  + " ( " + self.card_number + " )" 
