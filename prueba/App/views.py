from django.shortcuts import render
from django.http import HttpResponse
from .models import familiares

# Create your views here.
def prueba(request):
    return HttpResponse('Esto es una prueba')

def prueba_render(request):
    return render(request, "index.html", {})

def Familiar(request):
    familiar1=familiares(nombre="Mia Perez",edad=12,fn="2010-12-12")
    familiar1.save()
    familiar2=familiares(nombre="Esther Perez",edad=26,fn="1995-12-12")
    familiar2.save()
    familiar3=familiares(nombre="Luis Perez",edad=34,fn="1987-12-12")
    familiar3.save()
    lista_familiares=[familiar1, familiar2, familiar3]
    

    return render(request,"index.html", {"familiares":lista_familiares})
