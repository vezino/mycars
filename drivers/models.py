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
class Driver(models.Model):
  LICENSE_TYPE = (
    ("0","Tipo de licencia"),
    ("A","TIPO A "),
    ("B","TIPO B"),
    ("C","TIPO C"),
    ("D","TIPO D"),
    )
  BLOD_TYPE =(
    ("0","Seleccione el tipo de sangre"),
    ("1","O-"),
    ("2","O+"),
    ("3","A-"),
    ("4","A+"),
    ("5","B-"),
    ("6","B+"),
    ("7","AB-"),
    ("8","AB+"),
    )
  STATUS = (
    ("0","N/A"),
    ("1","activo"),
    ("2","inactivo"),
    )
  GENDER = (
    ("0","Masculino"),
    ("1","Femanino"),
    )
  STATE = (
    ("0","Seleccione el estado"),
    ("1","Aguascalientes     "),
    ("2","Baja California    "),
    ("3","Baja California Sur"),
    ("4","Campeche           "),
    ("5","Chiapas            "),
    ("6","Chihuahua          "),
    ("7","Ciudad de México   "),
    ("8","Coahuila           "),
    ("9","Colima             "),
    ("10","Durango          "),
    ("11","Estado de México "),
    ("12","Guanajuato       "),
    ("13","Guerrero         "),
    ("14","Hidalgo          "),
    ("15","Jalisco          "),
    ("16","Michoacán        "),
    ("17","Morelos          "),
    ("18","Nayarit          "),
    ("19","Nuevo León       "),
    ("20","Oaxaca           "),
    ("21","Puebla           "),
    ("22","Querétaro        "),
    ("23","Quintana Roo     "),
    ("24","San Luis Potosí  "),
    ("25","Sin Localidad    "),
    ("26","Sinaloa          "),
    ("27","Sonora           "),
    ("28","Tabasco          "),
    ("29","Tamaulipas       "),
    ("30","Tlaxcala         "),
    ("31","Veracruz         "),
    ("32","Yucatán          "),
    ("33","Zacatecas        "),
    )
  # General Driver data
  name = models.CharField("nombre/s",max_length=100)
  last_name = models.CharField("apellidos",max_length=100)
  photo = models.ImageField("Foto chofer:",upload_to="drivers/",default="")
  email = models.CharField("email",max_length=120,default="")
  birthdate = models.DateTimeField("fecha de nacimiento",default=datetime.now)
  blod_type = models.CharField("tipo de sangre",max_length=1,default= 0,choices = BLOD_TYPE)
  # License data
  license_type = models.CharField("tipo de licencia",max_length=1,default= 0,choices = LICENSE_TYPE)
  license_number =  models.CharField("numero de licencia",max_length=100)
  license_valid = models.DateTimeField("fecha de vencimiento",default=datetime.now)
  # Official id data
  ife_number = models.CharField("IFE",max_length=20,default=0)
  curp = models.CharField("CURP",max_length=18,default=0)
  # Address data 
  street = models.CharField("calle",max_length=20,default="")
  ext_number = models.CharField("número exterior",max_length=20,default="")
  int_number = models.CharField("numero interior",max_length=20,default=0)
  zip_code = models.CharField("codigo postal",max_length=5,default="")
  city = models.CharField("ciudad",max_length=20,default=0)
  state = models.CharField("estado",max_length=2,default= 0,choices = STATE)
  country = models.CharField("pais",max_length=20,default="México")
  # Driver status
  created_at = models.DateTimeField("fecha de alta",default=datetime.now)
  status = models.CharField("status del chofer",max_length=1,default= 0,choices = STATUS)  
  license_photo_front= models.ImageField("Foto licencia frente",upload_to="drivers/licence",default="",blank=True)
  license_photo_back = models.ImageField("Foto licencia reverso",upload_to="drivers/license",default="",blank=True)
  class Meta:
    verbose_name_plural = "choferes"

  def __str__(self):
    return self.name + " " + self.last_name