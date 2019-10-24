from django.shortcuts import render
from .models import Portada
from django.views.generic.list import ListView
# Create your views here.

class PortadaListView(ListView):
	template_name = 'portada/index.html'
	model = Portada
