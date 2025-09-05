# Create your models here.
from django.db import models

class Mesa(models.Model):
    STATUS_CHOICES = [
        ('livre', 'Livre'),
        ('ocupada', 'Ocupada'),
        ('reservada', 'Reservada'),
        ('atendimento', 'Em Atendimento')
    ]

    numero = models.PositiveIntegerField(unique=True)
    capacidade = models.PositiveIntegerField()
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='livre')
    reserva_data = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.numero} - {self.status}"
