# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Item
from .forms import CategoriaForm, ItemForm
from django.shortcuts import render
from pedidos.models import Pedido, ItemPedido
from cardapio.models import Item
from django.db.models import Sum, Count


# --- Categorias ---
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'cardapio/lista_categorias.html', {'categorias': categorias})

def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria criada com sucesso!')
        return redirect('lista_categorias')
    return render(request, 'cardapio/form_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        messages.success(request, 'Categoria atualizada com sucesso!')
        return redirect('lista_categorias')
    return render(request, 'cardapio/form_categoria.html', {'form': form})

def apagar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    messages.success(request, 'Categoria apagada!')
    return redirect('lista_categorias')

# --- Itens ---
def lista_itens(request):
    itens = Item.objects.select_related('categoria').all()
    return render(request, 'cardapio/lista_itens.html', {'itens': itens})

def criar_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item criado com sucesso!')
        return redirect('lista_itens')
    return render(request, 'cardapio/form_item.html', {'form': form})

def editar_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item atualizado com sucesso!')
        return redirect('lista_itens')
    return render(request, 'cardapio/form_item.html', {'form': form})

def apagar_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    messages.success(request, 'Item apagado!')
    return redirect('lista_itens')

# --- Relatório de Itens Mais Vendidos ---
def itens_mais_vendidos(request):
    itens_vendidos = ItemPedido.objects.values('item__nome').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:10]
    return render(request, 'cardapio/itens_mais_vendidos.html', {'itens_vendidos': itens_vendidos})

# --- Relatório de Vendas por Categoria ---
def vendas_por_categoria(request):
    vendas_categoria = ItemPedido.objects.values('item__categoria__nome').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')
    return render(request, 'cardapio/vendas_por_categoria.html', {'vendas_categoria': vendas_categoria})

# --- Relatório de Vendas Diárias ---
def vendas_diarias(request):
    vendas_diarias = Pedido.objects.values('criado_em__date').annotate(total_pedidos=Count('id')).order_by('-criado_em__date')
    return render(request, 'cardapio/vendas_diarias.html', {'vendas_diarias': vendas_diarias})

# --- Relatório de Itens com Baixa Disponibilidade ---
def itens_baixa_disponibilidade(request):
    itens_baixa = Item.objects.filter(disponivel=True).annotate(total_vendido=Sum('itens__quantidade')).filter(total_vendido__lt=5)
    return render(request, 'cardapio/itens_baixa_disponibilidade.html', {'itens_baixa': itens_baixa})

# --- Relatório de Itens Não Vendidos ---
def itens_nao_vendidos(request):
    itens_nao_vendidos = Item.objects.filter(itens__isnull=True)
    return render(request, 'cardapio/itens_nao_vendidos.html', {'itens_nao_vendidos': itens_nao_vendidos})

# --- Relatório de Vendas por Atendente ---
def vendas_por_atendente(request):
    vendas_atendente = Pedido.objects.values('atendente__username').annotate(total_pedidos=Count('id')).order_by('-total_pedidos')
    return render(request, 'cardapio/vendas_por_atendente.html', {'vendas_atendente': vendas_atendente})
def dashboard(request):
    # Total de pedidos por status
    pedidos_status = Pedido.objects.values('status').annotate(total=Count('id'))

    # Produtos mais vendidos
    produtos_vendidos = ItemPedido.objects.values('item__nome').annotate(total_vendido=Sum('quantidade')).order_by('-total_vendido')[:5]

    # Total de pedidos por tipo
    pedidos_tipo = Pedido.objects.values('tipo').annotate(total=Count('id'))

    context = {
        'pedidos_status': pedidos_status,
        'produtos_vendidos': produtos_vendidos,
        'pedidos_tipo': pedidos_tipo,
    }
    return render(request, 'cardapio/dashboard.html', context)

