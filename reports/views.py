from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.views import View
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
import unicodedata
from reports.forms import DateSelector, YearSelector

#Date
from datetime import date, timedelta, datetime
import datetime
import calendar
from django.utils import timezone
import pytz

# Parsing
import ast

# Model
from uber.models import VMycarsIncomeByYearMonth



#Add TIME_ZONE constant to use in get_utc method
TIME_ZONE = "America/Mexico_City"
# This method return the given time zone UTC
# Can use a diferent Time Zone with time_zone parameter
def get_utc(time_zone=TIME_ZONE):
  # Read current UTC datetime
  utc = pytz.utc.localize(datetime.datetime.utcnow())
  # Set users time zone
  instance_time_zone = pytz.timezone(time_zone)
  # Convert current UTC to user tome zone
  return utc.astimezone(instance_time_zone)

# Get month difference
def diff_month(start_date, end_date):
    return (start_date.year - end_date.year)*12 + start_date.month - end_date.month

# Method that adds months to a date... returns a full datetime object
def add_months(sourcedate, months):
  month = sourcedate.month - 1 + months
  year = int(sourcedate.year + month / 12 )
  month = month % 12 + 1
  day = min(sourcedate.day, calendar.monthrange(year,month)[1])
  return datetime.date(year,month,day)

# Get intial date array for all queries
def initialize_dates():
   # Called to get_utc method
    utc_mx = get_utc()

    start_date = add_months(utc_mx, -12)
    end_date = date(utc_mx.year,utc_mx.month,utc_mx.day)
    return [datetime.date(start_date.year,start_date.month,1), end_date]

def GetData(year):
  # Define variables:
  results = []
  row = []
  # Get data
  data = VMycarsIncomeByYearMonth.objects.filter(trip_year=year)
  # Define Header.
  #results.append(['Year','Month','Travels','Total Payment'])
  results.append(['Month','Travels','Total Payment'])
  # Fill array.
  for month in data:
    #print month.trip_month
    #row.append(month.trip_year)
    #row.append(month.trip_month)
    row.append(unicodedata.normalize('NFKD', month.trip_month).encode('ascii','ignore'))
    row.append(month.viajes)
    row.append(month.total_payment)
    results.append(row)
    row = [] 

  print '**************************'
  print results
  print '**************************'  
  return results

class Dashbord(View):
  template_name = 'dashbord.html'
  def get(self, request, *args, **kwargs):
    # Get initial dates
    start_dates = initialize_dates()
    start_date = start_dates[0]
    end_date = start_dates[1]
    # Get Data
    income = GetData(2016)
    form = YearSelector()
    print income
    return render(request, self.template_name,{"data":income, "form": form,})

  def post(self, request, *args, **kwargs):
    form = YearSelector(request.POST)
    if form.is_valid():
      #print "*****************************"
      #initial_date = form['from_date']
      selected_year = form.cleaned_data['report_year']
      print "*****************************" 
      print selected_year
      print "*****************************"
    income = GetData(selected_year)
    #form = DateSelector()
    print income
    return render(request, self.template_name,{"data":income, "form": form,})



