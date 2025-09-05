# Create your models here.
from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.FloatField()
    unidade = models.CharField(max_length=20, default='unidade')  # ex: kg, litro, unidade
    alerta_estoque = models.FloatField(default=5)  # quantidade mínima antes de alerta

    def __str__(self):
        return f"{self.nome} ({self.quantidade} {self.unidade})"


class Movimentacao(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    tipo = models.CharField(max_length=20, choices=[('entrada','Entrada'),('saida','Saída')])
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} {self.quantidade} de {self.ingrediente.nome}"
