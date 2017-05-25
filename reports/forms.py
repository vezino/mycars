# -*- encoding: utf-8 -*-
from django import forms
from django.forms import extras
#Date
from datetime import date, timedelta, datetime
# For UTC
import datetime
from django.utils import timezone
import pytz

# DATES form
class DateSelector(forms.Form):
  # Read current UTC datetime
  utc = pytz.utc.localize(datetime.datetime.utcnow())
  # Set users time zone
  instance_time_zone = pytz.timezone('America/Mexico_City')
  # Convert current UTC to user tome zone
  utc_mx = utc.astimezone(instance_time_zone)

  from_date = forms.DateField(
      required=True,
      label='Desde:',
      initial=date(utc_mx.year, 1, 1),
      widget=extras.SelectDateWidget(
              years=range(2014, 2020)
          ))
  until_date = forms.DateField(
      required=True,
      label='Hasta:',
      initial=date(utc_mx.year,utc_mx.month,utc_mx.day),
      widget=extras.SelectDateWidget(
              years=range(2014, 2020)
          ))

REPORT_YEARS = (
  (2015,"2015"),
  (2016,"2016"),
  (2017,"2017"),
  (2018,"2018"),
  (2019,"2019"),
  (2020,"2020"),
  )

REPORT_MONTHS = (
  (1,"January"),
  (2,"February"),
  (3,"March"),
  (4,"April"),
  (5,"May"),
  (6,"June"),
  (7,"July"),
  (8,"August"),
  (9,"September"),
  (10,"October"),
  (11,"November"),
  (12,"December"),    
  )
class YearSelector(forms.Form):
  #report_year = forms.DateField(widget=forms.SelectDateWidget(years=REPORT_YEARS))  
  report_year = forms.ChoiceField(widget=forms.Select, choices = REPORT_YEARS)

class MonthYearSelector(forms.Form):
  report_month = forms.ChoiceField(widget=forms.Select, choices = REPORT_MONTHS)
  report_year = forms.ChoiceField(widget=forms.Select, choices = REPORT_YEARS)






