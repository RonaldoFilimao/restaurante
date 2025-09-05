# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    """
    Model de usuário customizado para o sistema de restaurante.
    Inclui cargo, turno e evita conflito com auth.User.
    """

    CARGOS = [
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('atendente', 'Atendente'),
        ('cozinheiro', 'Cozinheiro'),
        ('caixa', 'Caixa'),
    ]

    TURNOS = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    cargo = models.CharField(max_length=20, choices=CARGOS, blank=True, null=True)
    turno = models.CharField(max_length=10, choices=TURNOS, blank=True, null=True)

    # Campos para evitar conflito com auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_custom',  # Evita conflito com auth.User.groups
        blank=True,
        help_text='Grupos aos quais o usuário pertence',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_custom_permissions',  # Evita conflito com auth.User.user_permissions
        blank=True,
        help_text='Permissões específicas do usuário',
        verbose_name='permissões do usuário'
    )

    def __str__(self):
        return f"{self.username} ({self.cargo})"
