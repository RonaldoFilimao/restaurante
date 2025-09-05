from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bem-vindo ao Sistema de Gestão do Restaurante!</h1>")
