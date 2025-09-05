from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lista_caixa(request):
    return HttpResponse("Lista do caixa")

def criar_caixa(request):
    return HttpResponse("Criar caixa")

def editar_caixa(request, pk):
    return HttpResponse(f"Editar caixa {pk}")

def apagar_caixa(request, pk):
    return HttpResponse(f"Apagar caixa {pk}")

