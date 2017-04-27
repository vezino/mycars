# coding=utf-8
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from uber.models import UploadUberData, UberData
from django.utils import timezone
from django.urls import reverse_lazy
#from django import forms
from uber.forms import UploadUberDataForm
# Messages
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect, HttpResponse
# csv
import csv
# open file from url
import urllib2
import unicodedata
from django.utils.encoding import python_2_unicode_compatible
# Create your views here.
# import sys
# reload(sys)
# #sys.setdefaultencoding('utf8')
# sys.setdefaultencoding('latin-1')


class UploadUberDataListView(ListView):
  model = UploadUberData
  template = "uber/UberUploadFileList.html"
  def get_context_data(self, **kwargs):
    context = super(UploadUberDataListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

# class UploadUberDataCreateView(CreateView):
#   model = UploadUberData
#   template = "uber/uploaduberdata_form"
#   fields = ['name','uber_file_uploaded','file_procesed']
#   success_url = reverse_lazy('Dashbord')
#@python_2_unicode_compatible
class UploadUberDataCreateView(View):
  template_name = "uploaduberdata_form.html"
  def get(self, request, *args, **kwargs):
    form = UploadUberDataForm()
    income = 0
    return render(request, self.template_name,{"form": form,})

  def post(self, request, *args, **kwargs):
    form = UploadUberDataForm(request.POST,request.FILES)
    #print from.name
    if form.is_valid():
      form_object = form.save()
      #messages.success(request, "Los datos de uber fueron actualizados exitosamente.")
      print '***********************************'
      print form_object.id
      print form_object.uber_file_uploaded.url
      print '***********************************'
      valid_load = write_uberdata(form_object.uber_file_uploaded.url,request)
      if valid_load:
        messages.success(request, "Los datos de uber fueron actualizados exitosamente.")
        return HttpResponseRedirect('/reports')
      else:
        form_object.delete()
        messages.error(request, "Error al cargar el archivo CSV.")
          
      # data = urllib2.urlopen(form_object.uber_file_uploaded.url) 
      # reader = csv.DictReader(data)
      #reader = reader.encode('utf-8')
      #return HttpResponseRedirect('/reports')
 
    return render(request, self.template_name,{"form": form,})
# Write uploded csv data to uberdata table
def write_uberdata(file_url,request):
  data = urllib2.urlopen(file_url)
  reader = csv.DictReader(data)
  valid_load = True
  for idx,row in enumerate(reader):
    #print row['Driver Name'].encode('utf-8') ,row['Phone Number'] , row['Surge']
    if row['Type'] == 'Trip':
      try:
        loaduberdata = UberData(
          driver_name = row['Driver Name'].decode('latin-1').encode('utf-8'),
          phone_number = row['Phone Number'],
          email = row['Email'],
          trip_type = row['Type'],
          trip_date = row['Date'],
          description = row['Description'],
          trip_number = row['Trip #'],
          fare = 0 if row['Fare'] == "" else float(row['Fare']),
          surge = 0 if row['Surge'] == "" else float(row['Surge']),
          toll = 0 if row['Toll'] == "" else float(row['Toll']),
          misc = 0 if row['Misc'] == "" else float(row['Misc']),
          other = 0 if row['Other'] == "" else float(row['Other']),
          meter_rate = 0 if row['Meter Rate'] == "" else float(row['Meter Rate']),
          gratuity = 0 if row['Gratuity'] == "" else float(row['Gratuity']),
          commission = 0 if row['Commission'] == "" else float(row['Commission']),
          tax_on_fee = 0 if row['Tax on Fee'] == "" else float(row['Tax on Fee']),
          total_payment = 0 if row['Total Payment'] == "" else float(row['Total Payment'])
          )
        loaduberdata.save()
      except Exception as e:
        valid_load = False
        print "************** Error Data ****************"
        print row 
        print "******************************************"
        print 
        #print row['Driver Name'].decode('utf-8')
        #print row['Driver Name'].encode('latin-1')
        #print row['Driver Name'].decode('latin-1')
        print e
        print "********* Linea ************"
        print idx
        print "****************************"
        #print row['Driver Name']
        #print e,  row['Driver Name']
        error_line = "Error en la linea %s al leer el archivo CSV" % str(idx+1)   
        messages.error(request, error_line)
        break  
        #.encode('utf-8','replace')
        #return HttpResponseRedirect('/uber')
#    else:
#      messages.error(request, "Error al cargar el archivo CSV.")   
  return valid_load

