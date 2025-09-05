from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de URLs da app usuarios
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:pk>/apagar/', views.apagar_usuario, name='apagar_usuario'),
]
