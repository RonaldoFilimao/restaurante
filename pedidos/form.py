from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produto', 'quantidade', 'status']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'produto': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'quantidade': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full'}),
            'status': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
        }
