# Register your models here.
from django.contrib import admin
from .models import Ingrediente, Movimentacao

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'unidade', 'alerta_estoque')
    search_fields = ('nome',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('ingrediente', 'quantidade', 'tipo', 'data')
    list_filter = ('tipo', 'data')
