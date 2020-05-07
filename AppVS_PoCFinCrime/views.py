from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

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

def Clientes(request):
    
        return render(
        request,
        "AppVS_PoCFinCrime/Clientes.html",
        {
            'title' : "Clientes",
            'content' : "Contenido de la tabla de Clientes2."
        }
    )

def Transacciones(request):
    return render(
        request,
        "AppVS_PoCFinCrime/Transacciones.html",
        {
            'title' : "Transacciones",
            'content' : "Contenido de la tabla de Transacciones2."
        }
    )


def Cuentas(request):
    return render(
        request,
        "AppVS_PoCFinCrime/Cuentas.html",
                {
            'title' : "Cuentas",
            'content' : "Contenido de la tabla de Cuentas2."
        }
    )