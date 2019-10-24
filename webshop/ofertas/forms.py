from django import forms
from .models import Ofertas
from core.models import Subscriptores

class OfertaForm(forms.ModelForm):
	
	class Meta:
		valor = Subscriptores.objects.all();
		val = len(valor)
		model = Ofertas
		fields = '__all__'
		widgets = {
			'titulo': forms.TextInput(),
			'asunto': forms.TextInput(),
			'descripcion': forms.Textarea(attrs={'name':'editor','id':'editor'}),
			'destinatarios':forms.NumberInput(attrs={'value':val,'readonly':''}),
		}
		labels = {
			'titulo':'Título:','asunto':'Asunto:', 'descripcion' : 'Descripción:',
		}