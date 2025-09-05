# Create your models here.
from django.db import models
from pedidos.models import Pedido
from usuarios.models import Usuario

class LogVenda(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    atendente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda Pedido #{self.pedido.id} - {self.total}"
