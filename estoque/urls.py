from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estoque, name='lista_estoque'),
    path('criar/', views.criar_item_estoque, name='criar_item_estoque'),
    path('<int:pk>/editar/', views.editar_item_estoque, name='editar_item_estoque'),
    path('<int:pk>/apagar/', views.apagar_item_estoque, name='apagar_item_estoque'),
]
