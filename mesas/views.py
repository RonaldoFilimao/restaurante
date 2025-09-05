from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lista_mesas(request):
    return HttpResponse("Lista de mesas")

def criar_mesa(request):
    return HttpResponse("Criar mesa")

def editar_mesa(request, pk):
    return HttpResponse(f"Editar mesa {pk}")

def apagar_mesa(request, pk):
    return HttpResponse(f"Apagar mesa {pk}")

