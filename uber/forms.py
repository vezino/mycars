# -*- encoding: utf-8 -*-
from django import forms
from django.forms import extras
#Date
from datetime import date, timedelta, datetime
# For UTC
import datetime
from django.utils import timezone
import pytz
from uber.models import UploadUberData


# DATES form
# class DateSelector(forms.Form):
#   # Read current UTC datetime
#   utc = pytz.utc.localize(datetime.datetime.utcnow())
#   # Set users time zone
#   instance_time_zone = pytz.timezone('America/Mexico_City')
#   # Convert current UTC to user tome zone
#   utc_mx = utc.astimezone(instance_time_zone)

#   from_date = forms.DateField(
#       required=True,
#       label='Desde:',
#       initial=date(utc_mx.year, 1, 1),
#       widget=extras.SelectDateWidget(
#               years=range(2014, 2020)
#           ))
#   until_date = forms.DateField(
#       required=True,
#       label='Hasta:',
#       initial=date(utc_mx.year,utc_mx.month,utc_mx.day),
#       widget=extras.SelectDateWidget(
#               years=range(2014, 2020)
#           ))

# REPORT_YEARS = (
#   (2015,"2015"),
#   (2016,"2016"),
#   (2017,"2017"),
#   (2018,"2018"),
#   )

# class YearSelector(forms.Form):
#   #report_year = forms.DateField(widget=forms.SelectDateWidget(years=REPORT_YEARS))  
#   report_year = forms.ChoiceField(widget=forms.Select, choices = REPORT_YEARS)

class UploadUberDataForm(forms.ModelForm):
  class Meta:
    model = UploadUberData
    fields = ['name','uber_file_uploaded']
    labels = {
              'name':'Uber Data Name',
              'uber_file_uploaded':'Uber Data File'
    }
    #widgets = {'uber_file_uploaded' : forms.FileField({'is_hidden': 'True'})},
    widgets = {
               'name': forms.TextInput(attrs={'placeholder':'eg: Input 2017/04/13'}),
               'uber_file_uploaded' : forms.FileInput({'is_hidden': 'False'})

     }

  def clean_uber_file_uploaded(self):
    upload_file = self.cleaned_data.get('uber_file_uploaded', False)
    print upload_file.content_type
    if self.files:
      main, sub = upload_file.content_type.split('/')
      if not (main == 'text' and sub.lower() in ['csv',]):
                raise forms.ValidationError(('Use una archivo CSV.'))
    return upload_file







