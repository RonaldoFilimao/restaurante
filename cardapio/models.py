# Create your models here.
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Item(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='itens')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ingredientes = models.TextField(blank=True)
    foto = models.ImageField(upload_to='cardapio_fotos/', blank=True, null=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.categoria.nome}"
