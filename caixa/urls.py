from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_caixa, name='lista_caixa'),
    path('criar/', views.criar_caixa, name='criar_caixa'),
    path('<int:pk>/editar/', views.editar_caixa, name='editar_caixa'),
    path('<int:pk>/apagar/', views.apagar_caixa, name='apagar_caixa'),
]
