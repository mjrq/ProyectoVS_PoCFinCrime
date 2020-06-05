from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import datetime

from AppVS_PoCFinCrime.models import CUSTOMERS
from django.views import generic
from django_tables2 import SingleTableView

from .forms import ClientesForm


import csv, io
import codecs
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# one parameter named request
def CargarClientes(request):
    # declaring template
    template = "AppVS_PoCFinCrime/CargarClientes.html"
    data = CUSTOMERS.objects.all()
    #prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV must be according to the model',
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

    
    # Read complete CSV
    data_set = csv_file.read().decode('latin-1')

    # Read CSV lines 
    lines = data_set.split("\n")

    #Get the data from CSV
    for line in lines:
        #Data separate by "|"
        data=line.split("|")
        
        #Convert empty fields in nullable data and Create a list with all data.
        fields =[]
        for i in data:
            if i=='':
                fields.append(None)
            else:
                fields.append(i)
        #Create table
        CUSTOMER = CUSTOMERS(ACCOUNT_BALANCE =float(fields[0]) if (fields[0] is not None) else fields[0],
                             ACCOUNT_ON_HOLD_FLAG = fields[1],
                             ACCOUNT_PURPOSE =fields[2],
                             ACCOUNT_SEGMENT =int(fields[3]),
                             ACCOUNT_SOURCE_UNIQUE_ID =fields[4],
                             ACCOUNT_STATUS_CODE =fields[5],
                             ACQUISITION_DATE = datetime.strptime(fields[6],'%Y'),
                             ANN_PREMIUM_AMT = fields[7],
                             BALANCE_DATE = datetime.strptime(fields[8],'%Y'),
                             BENEFICIARY_FLAG =fields[9],
                             BLOCKED_REASON =  fields[10],                                 
                             BLOCKED_TYPE = fields[11],                                  
                             BRANCH_ID =int(fields[12]),
                             BUSINESS_SEGMENT_1 = fields[13],
                             BUSINESS_TYPE =fields[14],
                             CANCELLED_DATE = fields[15],
                             CASH_SURR_VALUE = fields[16],
                             CHANNEL_OF_OPENING = fields[17],
                             CHECK_ACCOUNT_NUMBER = int(fields[18]),
                             CITY = fields[19],
                             COLLECTED_BALANCE =float(fields[20])  if (fields[20] is not None) else fields[20], 
                             COMMENTS =fields[21], 
                             COMPANY_FORM  = fields[22], 
                             COMPANY_NAME =fields[23], 
                             COUNTRY_OF_ORIGIN = fields[24], 
                             COUNTRY_OF_RESIDENCE = fields[25], 
                             CREDIT_DEBIT_CODE =fields[26],
                             CREDIT_LIMIT = float(fields[27]) if (fields[27] is not None) else fields[27],
                             CREDIT_TURNOVER = fields[28],
                             CURRENCY_CODE =fields[29], 
                             CURRENCY_CODE_BASE = fields[30],
                             CURRENCY_CODE_ORIG = fields[31],
                             CUSTOMER_INITIATED_CLOSURE = fields[32],
                             CUSTOMER_SEGMENT_1 =int(fields[33]),
                             CUSTOMER_SOURCE_UNIQUE_ID = fields[34],
                             CUSTOMER_ID =fields[35],
                             CUSTOMER_STATUS_CODE = int(fields[36]),
                             CUSTOMER_TYPE = fields[37],
                             CUSTOMER_TYPE_CODE = fields[38],
                             DATE_CLOSED = datetime.strptime(fields[39],'%d/%m/%Y'),
                             DATE_OPENED = datetime.strptime(fields[40],'%d/%m/%Y'),
                             DEATH_BENEFIT_AMT =fields[41],
                             DEBIT_TRUNOVER =fields[42],
                             DELAYED_ACCOUNT_FLAG = fields[43],
                             DELIVERY_INSTRUCTIONS = fields[44],
                             DEVICE_ID = fields[45],
                             EMPLOYEE_FLAG = fields[46],
                             EMPLOYEE_NUMBER = fields[47],
                             EMPLOYMENT_STATUS = fields[48],
                             ERROR_CORRECT_FLAG =fields[49],
                             FILTER = fields[50],
                             FROM_DATE =datetime.strptime(fields[51],'%d/%m/%Y'),
                             GENDER_CODE = fields[52],
                             GROSS_PREM_TTD =fields[53],
                             HOLDING_BANK_NAME = fields[54],
                             INCORPORATION_COUNTRY_CODE = fields[55],
                             INCORPORATION_DATE = datetime.strptime(fields[56],'%d/%m/%Y'),
                             INST_PREMIUM_AMT = fields[57],
                             ISSUE_DATE = datetime.strptime(fields[58],'%d/%m/%Y'),
                             LANGUAGE_PREF_CODE = fields[59],
                             LIFE_INS_CONTRACT_DURATION = int(fields[60]),
                             MATURITY_DATE =fields[61],
                             OCCUPATION =fields[62],
                             ORG_UNIT_CODE = fields[63],
                             ORIGINATION_DATE =datetime.strptime(fields[64],'%d/%m/%Y'),
                             OTHER_HOLD_AMOUNT = float(fields[65])  if (fields[65] is not None) else fields[65],
                             OVERDRAFT_LIMIT =float(fields[66])  if (fields[66] is not None) else fields[66],
                             PAYMENT_FREQ = fields[67],
                             PAYMENT_METHOD = fields[68],
                             PERIODIC_LOAN_AMOUNT =float(fields[69]  if (fields[69] is not None) else fields[69]),
                             PERSON_TITLE = fields[70],
                             POSTAL_CODE =int(fields[71]),
                             PRIMARY_CARD_ID =fields[72],
                             PRIMARY_CUSTOMER_CATEGORY_CODE = fields[73],
                             PRIME_BRANCH_ID =int(fields[74]),
                             PRODUCT_SOURCE_TYPE_CODE = fields[75],
                             REGISTERED_NUMBER =fields[76],
                             RELATIONSHIP_MGR_ID =int(fields[77]),
                             REPORTING_REGION =fields[78],
                             RISK_CATEGORY = fields[79],
                             RISK_SCORE =int(fields[80]),
                             RUN_TIMESTAMP =fields[81],
                             SALARY_LODGED_FLAG = fields[82],
                             SENT_CORRESPONDENCE_FLAG =fields[83],
                             SETTLEMENT_BANK_NAME =fields[84],
                             SETTLEMENT_TYPE = fields[85],
                             SINGLE_PREMIUM_TOTAL = fields[86],
                             SOURCE_SYSTEM_CODE = fields[87],
                             SOURCE_TXN_NUM = fields[88],
                             SOURCE_TXN_UNIQUE_ID = fields[89],
                             SUB_DIVISION =fields[90],
                             SUM_INSURED =fields[91],
                             TO_DATE = fields[92],
                             TOTAL_DEPOSITS_BASE = fields[93],
                             TOTAL_LOANS_BASE = int(fields[94]),
                             TRANSACTION_LOCATION = fields[95],
                             TURNOVER_FROM_DATE =fields[96],
                             TURNOVER_TO_DATE =fields[97],
                             TXN_AMOUNT_ORIG = float(fields[98])  if (fields[98] is not None) else fields[98],
                             TXN_CHANNEL_CODE = fields[99],
                             TXN_SOURCE_TYPE_CODE = fields[100],
                             TXN_STATUS_CODE = fields[101],
                             ZONE = fields[102]                                
                             )
        CUSTOMER.save()

    context = {}
    template2 = "AppVS_PoCFinCrime/FicheroCargado.html" 
    return render(request, template2, context)

class ListaClientes(SingleTableView):
    model = CUSTOMERS
    context_object_name = 'customers_list'   # your own name for the list as a template variable
    template_name = 'customers_list.html' # Specify your own template name/location

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
    
