from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.views import View
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
import unicodedata
from reports.forms import DateSelector, YearSelector, MonthYearSelector
from django.db.models import Count, Avg
#Date
from datetime import date, timedelta, datetime
import datetime
import calendar
from django.utils import timezone
import pytz
from collections import defaultdict

# Parsing
import ast

# Model
from uber.models import VMycarsIncomeByYearMonth, VMyCarsIncomeByDriverYearMonthWeek, VMycarsFilterDriverMonthYear
# Panda
from django_pandas.io import read_frame
import json
#import numpy
import numpy as np

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
def initialize_dates(months_before):
   # Called to get_utc method
    utc_mx = get_utc()

    start_date = add_months(utc_mx, months_before)
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


class DriversTripReport(View):
  template_name = 'DriversTripReport.html'
  def get(self, request, *args, **kwargs):
    #form = MonthYearSelector()
    form = DateSelector()
    # Get initial dates
    start_dates = initialize_dates(-5)
    start_date = start_dates[0]
    end_date = start_dates[1]
    print start_dates
    print start_date
    print end_date
    # Define columns to Retrive
    select_columns = ['date','phone_number','viajes']
    # Define Pivot definition
    pivot_def ={'index': 'date', 'columns': 'phone_number', 'values':'viajes'}
    # Get data
    #income = GetDriverTripsData(start_date,end_date,select_columns,pivot_def)
    #stats = GetDriverTripStats(start_date,end_date,select_columns,pivot_def)
   
    #print income
    #return render(request, self.template_name,{"data":income,"stats":stats, "form": form,})
    results = GetDriverTripsData(start_date,end_date,select_columns,pivot_def)

    return render(request, self.template_name,{"data":results['data'],"stats":results['stats'], 'sums':results['sums'],'totals':results['totals'],"form": form,})


  def post(self, request, *args, **kwargs):
    #form = MonthYearSelector(request.POST)
    form = DateSelector(request.POST)
    select_columns = ['date','phone_number','viajes']
    pivot_def ={'index': 'date', 'columns': 'phone_number', 'values':'viajes'}    
    if form.is_valid():
    #   income = GetDriverTripsData(form.cleaned_data['from_date'],form.cleaned_data['until_date'],select_columns,pivot_def)
    #   stats = GetDriverTripStats(form.cleaned_data['from_date'],form.cleaned_data['until_date'],select_columns,pivot_def)
    # #return render(request, self.template_name,{"data":income, "form": form,})
    # return render(request, self.template_name,{"data":income,"stats":stats, "form": form,})

      results = GetDriverTripsData(form.cleaned_data['from_date'],form.cleaned_data['until_date'],select_columns,pivot_def)
    return render(request, self.template_name,{"data":results['data'],"stats":results['stats'], 'sums':results['sums'],'totals':results['totals'],"form": form,})    

class DriversPaymentReport(View):
  template_name = 'DriversPaymentReport.html'
  def get(self, request, *args, **kwargs):
    #form = MonthYearSelector()
    form = DateSelector()
    # Get initial dates
    start_dates = initialize_dates(-6)
    #print start_dates
    start_date = start_dates[0]
    end_date = start_dates[1]
    # Define columns to Retrive
    select_columns = ['date','phone_number','total_payment']
    # Define Pivot definition
    pivot_def ={'index': 'date', 'columns': 'phone_number', 'values':'total_payment'}
    # Get Initial Data
    results = GetDriverTripsData(start_date,end_date,select_columns,pivot_def)

    return render(request, self.template_name,{"data":results['data'],"stats":results['stats'], 'sums':results['sums'],'totals':results['totals'],"form": form,})

  def post(self, request, *args, **kwargs):
    form = DateSelector(request.POST)
    select_columns = ['date','phone_number','total_payment']
    pivot_def ={'index': 'date', 'columns': 'phone_number', 'values':'total_payment'}    
    if form.is_valid():
      results = GetDriverTripsData(form.cleaned_data['from_date'],form.cleaned_data['until_date'],select_columns,pivot_def)

    return render(request, self.template_name,{"data":results['data'],"stats":results['stats'], 'sums':results['sums'],'totals':results['totals'],"form": form,})

# Get data from 
def GetDriverTripsData(ini_date,end_date,select_columns,pivot_def):
  #template_name = 'dashbord.html'
  # Define QuerySet:
  #qs = VMyCarsIncomeByDriverYearMonthWeek.objects.filter(year=year,month=month)
  qs = VMyCarsIncomeByDriverYearMonthWeek.objects.filter(date__range=[ini_date,end_date])
  print qs.count()
  if qs.count() != 0:
    # Read DataFranme and select columns to use
    #df = read_frame(qs,fieldnames=['date','phone_number','viajes'])
    df = read_frame(qs,fieldnames=select_columns)
    # Pivot data
    #df = df.pivot(index='date',columns='phone_number',values='viajes')
    df = df.pivot(index=pivot_def['index'],columns=pivot_def['columns'],values=pivot_def['values'])
    # Convert nan to 0
    data = df.fillna(value=0)
    # Sum columns
    #sums = df.groupby('date').aggregate(np.sum)
    sums = data.apply(np.cumsum)
    sums = sums.fillna(value=0)
    # Get Statistics
    df2 = df.describe()
    stats = df2.fillna(value=0)
    # print "************ stats"
    # print stats
    # print "************ sums"
    # print sums
    # print "************ data"
    # print data
    json_data = data.to_json(orient="split")
    json_sums = sums.to_json(orient="split")
    json_stat = stats.to_json(orient="split")


    return {
          'data':TranslateJSONResults(json_data,'Date'),
          'sums':TranslateJSONResults(json_sums,'Date'),
          'stats':TranslateJSONResults(json_stat,'Indicador'),
          'totals':ResultsTotals(TranslateJSONResults(json_sums,'Date'),'Totals')
          }
  else:
    print date.today()
    null_data = [['Date','No Data'],[str(date.today()),'0']]
    return {
          'data': null_data,
          'sums': null_data,
          'stats': null_data,
          'totals': null_data,
    }
 
     
# Convert json data to list
def TranslateJSONResults(json_data,extra_column):
  # Converty json to valid dict  
  json_dict = ast.literal_eval(json_data)
  # Separete Lists
  data_columns = json_dict['columns']
  data_index = json_dict['index']
  data_data = json_dict['data']
  # Insert Missing Date Header to columns
  data_columns.insert(0,extra_column)
  # Insert Index Date to Value
  results = []
  results.append(data_columns)
  for i,date in enumerate(data_index):
    data_data[i].insert(0,date)
  # Merge Header and data
  merged_data =  results + data_data
  # Return list 
  return merged_data

def ResultsTotals(sums,extra_column):
  # print sums
  # print len(sums)
  # print sums[0]
  # print sums[len(sums)-1]
  row_elements = sums[len(sums)-1]
  header = sums[0]
  header.append('Total')
  header[0]= 'Period Total'
  #print header
  total = 0
  for i,column in enumerate(row_elements):
    # print i
    # print column
    if i != 0:
      total += column
  #print total
  row_elements.append(total)
  #print row_elements
  results = []
  results.append(header)
  results.append(row_elements)
  print results
  
  return results



