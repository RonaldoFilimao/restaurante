# Register your models here.
from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'status', 'mesa', 'cliente_nome', 'criado_em', 'atendente')
    list_filter = ('tipo', 'status', 'criado_em')
    search_fields = ('cliente_nome',)
    inlines = [ItemPedidoInline]
