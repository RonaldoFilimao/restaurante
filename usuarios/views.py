from django.shortcuts import render

# Create your views here.
# usuarios/views.py
from django.http import HttpResponse

def lista_usuarios(request):
    return HttpResponse("Lista de usuários")

def criar_usuario(request):
    return HttpResponse("Criar usuário")

def editar_usuario(request, pk):
    return HttpResponse(f"Editar usuário {pk}")

def apagar_usuario(request, pk):
    return HttpResponse(f"Apagar usuário {pk}")

