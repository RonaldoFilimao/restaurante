# Create your models here.
from django.db import models
from pedidos.models import Pedido
from usuarios.models import Usuario

class Pagamento(models.Model):
    METODOS = [
        ('dinheiro', 'Dinheiro'),
        ('cartao', 'Cartão'),
        ('pix', 'PIX'),
        ('mpesa', 'M-Pesa')
    ]

    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODOS)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    caixa = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Pagamento Pedido #{self.pedido.id} - {self.metodo}"
