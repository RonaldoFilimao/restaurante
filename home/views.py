from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user

    # Definindo permissões com base em grupos
    context = {
        'can_view_dashboard': user.has_perm('home.view_dashboard'),
        'can_view_pedidos': user.has_perm('pedidos.view_pedido'),
        'can_view_cardapio': user.has_perm('cardapio.view_produto'),
        'can_view_caixa': user.has_perm('caixa.view_caixa'),
        'can_view_relatorios': user.has_perm('relatorios.view_relatorio'),
        'can_view_configuracoes': user.has_perm('configuracoes.change_configuracao'),
    }

    return render(request, 'home/dashboard.html', context)
