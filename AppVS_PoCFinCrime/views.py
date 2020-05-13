from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import datetime

from AppVS_PoCFinCrime.models import CUSTOMERS
from django.views import generic


import csv, io
import codecs
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# one parameter named request
def CargarClientes(request):
    # declaring template
    template = "AppVS_PoCFinCrime/CargarClientes.html"
    data = CUSTOMERS.objects.all()
# prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data,
        'title' : 'Load CSV file'
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    lines = data_set.split("\n")

    for line in lines:
        fields=line.split("|")
        data_dict = {}
        data_dict["CUSTOMER_SOURCE_UNIQUE_ID"] = fields[0]
        data_dict["first_name"] = fields[1]
        data_dict["last_name"] = fields[2]

        CUSTOMER = CUSTOMERS(CUSTOMER_SOURCE_UNIQUE_ID=fields[0],first_name=fields[1],last_name=fields[2])
        CUSTOMER.save()

    context = {}
    template2 = "AppVS_PoCFinCrime/FicheroCargado.html" 
    return render(request, template2, context)

class ListaClientes(generic.ListView):
    model = CUSTOMERS
    context_object_name = 'customers_list'   # your own name for the list as a template variable
    template_name = 'ClientesView.html' # Specify your own template name/location

def index(request):
    now = datetime.now()

    return render(
        request,
        "AppVS_PoCFinCrime/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
             'title' : "Inicio",
            'message' : "Pagina Principal PoCFinCrime",
           
        }
    )

def home(request):
    now = datetime.now()

    return render(
        request,
        "AppVS_PoCFinCrime/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Inicio",
            'message' : "Pagina Principal PoCFinCrime",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )



def BorrarClientes(request):
    CUSTOMERS.objects.all().delete()
    template = "AppVS_PoCFinCrime/BorrarClientes.html"   
    context = {}
    return render(request, template, context)


def CrearClientes(request):
    
    now = datetime.now()
    Cliente = CUSTOMERS(CUSTOMER_SOURCE_UNIQUE_ID=now.strftime("%A, %d %B, %Y at %X"),first_name='Nombre1',last_name='Nombre2')
    Cliente.save()
    
   
    return render_to_response("AppVS_PoCFinCrime/CrearClientes.html", {'Cliente': Cliente})
    
