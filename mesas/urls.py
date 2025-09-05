from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mesas, name='lista_mesas'),
    path('criar/', views.criar_mesa, name='criar_mesa'),
    path('<int:pk>/editar/', views.editar_mesa, name='editar_mesa'),
    path('<int:pk>/apagar/', views.apagar_mesa, name='apagar_mesa'),
]
