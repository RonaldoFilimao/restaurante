# Create your models here.
from django.db import models
from usuarios.models import Usuario
from mesas.models import Mesa
from cardapio.models import Item

class Pedido(models.Model):
    TIPO_CHOICES = [
        ('mesa', 'Mesa'),
        ('takeaway', 'Takeaway'),
        ('delivery', 'Delivery')
    ]

    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('preparo', 'Em Preparo'),
        ('pronto', 'Pronto'),
        ('entregue', 'Entregue')
    ]

    mesa = models.ForeignKey(Mesa, on_delete=models.SET_NULL, null=True, blank=True)
    cliente_nome = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atendente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.tipo} - {self.status}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.item.nome}"
