# Register your models here.
from django.contrib import admin
from .models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidade', 'localizacao', 'status', 'reserva_data')
    list_filter = ('status',)
    search_fields = ('numero', 'localizacao')
