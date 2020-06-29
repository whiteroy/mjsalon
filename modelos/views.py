from django.shortcuts import render
from .models import Empresa

# Create your views here.

def home (request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'home', 'nosotros': empresa}
    return render(request,'home.html', context)

def jefe(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'jefe.html', context)

def citas(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'citas.html', context)

def ac_caja(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'ac_caja.html', context)

def ver_citas(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'ver_citas.html', context)

def puntoventa(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'puntoventa.html', context)

def formapago(request):
    empresa = Empresa.objects.get(id=1)
    context = {'title': 'jefe', 'nosotros': empresa}
    return render(request,'formapago.html', context)