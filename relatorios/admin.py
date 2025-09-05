# Register your models here.
from django.contrib import admin
from .models import LogVenda

@admin.register(LogVenda)
class LogVendaAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'total', 'atendente', 'data')
    list_filter = ('data', 'atendente')
    search_fields = ('pedido__id', 'atendente__username')
