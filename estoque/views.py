from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def lista_estoque(request):
    return HttpResponse("Lista de estoque")

def criar_item_estoque(request):
    return HttpResponse("Criar item de estoque")

def editar_item_estoque(request, pk):
    return HttpResponse(f"Editar item de estoque {pk}")

def apagar_item_estoque(request, pk):
    return HttpResponse(f"Apagar item de estoque {pk}")

