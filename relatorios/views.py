from django.shortcuts import render

# Create your views here.
# Exemplo para caixa/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página inicial do Caixa")
