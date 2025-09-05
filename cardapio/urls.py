from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Categorias
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/apagar/', views.apagar_categoria, name='apagar_categoria'),

    # Itens
    path('itens/', views.lista_itens, name='lista_itens'),
    path('itens/criar/', views.criar_item, name='criar_item'),
    path('itens/<int:pk>/editar/', views.editar_item, name='editar_item'),
    path('itens/<int:pk>/apagar/', views.apagar_item, name='apagar_item'),

    # Relatórios
    path('relatorios/itens-mais-vendidos/', views.itens_mais_vendidos, name='itens_mais_vendidos'),
    path('relatorios/vendas-por-categoria/', views.vendas_por_categoria, name='vendas_por_categoria'),
    path('relatorios/vendas-diarias/', views.vendas_diarias, name='vendas_diarias'),
    path('relatorios/itens-baixa-disponibilidade/', views.itens_baixa_disponibilidade, name='itens_baixa_disponibilidade'),
    path('relatorios/itens-nao-vendidos/', views.itens_nao_vendidos, name='itens_nao_vendidos'),
    path('relatorios/vendas-por-atendente/', views.vendas_por_atendente, name='vendas_por_atendente'),
]
