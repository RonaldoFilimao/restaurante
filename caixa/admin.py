# Register your models here.
from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'valor_total', 'metodo', 'data_pagamento', 'caixa')
    list_filter = ('metodo', 'data_pagamento')
    search_fields = ('pedido__id', 'caixa__username')
