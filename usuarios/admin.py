from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'cargo', 'turno', 'is_staff', 'is_active')
    list_filter = ('cargo', 'turno', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email', 'cpf_nif', 'contato')}),
        ('Permissões', {'fields': ('cargo', 'turno', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    search_fields = ('username', 'email', 'cpf_nif')
    ordering = ('username',)

admin.site.register(Usuario, UsuarioAdmin)


# Register your models here.
