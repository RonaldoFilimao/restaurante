"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Página inicial
    path('admin/', admin.site.urls),
    # URLs das apps
    path('cardapio/', include('cardapio.urls')),      # Todas as URLs da app cardapio
    path('usuarios/', include('usuarios.urls')),      # Se tiver app usuarios
    path('mesas/', include('mesas.urls')),            # Se tiver app mesas
    path('pedidos/', include('pedidos.urls')),        # Se tiver app pedidos
    path('estoque/', include('estoque.urls')),        # Se tiver app estoque
    path('caixa/', include('caixa.urls')),            # Se tiver app caixa
    path('relatorios/', include('relatorios.urls')),  # Se tiver app relatorios
]
