from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import datetime

from AppVS_PoCFinCrime.models import CUSTOMERS
from django.views import generic

import pandas as pd
import pandas_profiling

import csv, io
import codecs
from datetime import datetime
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
# one parameter named request
def AnalisisInicial(request):
    template = "AppVS_PoCFinCrime/AnalisisInicial.html"
    data = CUSTOMERS.objects.all()
    print(data.values())
    context = {}
    if request.method == 'GET':
        #test_file = request.FILES.get(u'testFile')
        #if test_file:
        df = pd.DataFrame(data=list(data.values()),index=data['id'].values())
        #df.set_index(df.columns['id'])
        df = df.reset_index().drop('index',1)
        df.to_csv('prueba.csv')
        print(df.shape)
        #df = pd.read_csv(test_file)
        profile=df.profile_report(title='Análisis Preliminar ')
        profile.to_file(output_file='AppVS_PoCFinCrime/output2.html')
        context['df'] = df
        #print(df)
        #else:
            #messages.warning(request, f'No file to process! Please upload a file to process.')
   #template = "AppVS_PoCFinCrime/output.html"
    return render(request, template, context)
