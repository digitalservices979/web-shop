from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import json
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Prenda
from portada.models import Portada
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class PackageListView(ListView):
	template_name = 'packages/package.html'
	model = Prenda
	paginate_by = 9


class PrendaDetailView(DetailView):
	template_name = "packages/detalle.html"
	@csrf_exempt
	def get(self, request, pk):
		objecto = Portada.objects.get(pk=1)
		try:
			objecto = Portada.objects.get(pk=pk)
			paypal_dict = {
			"business" : 'qwer_jv16@outlook.com',
			"amount" : objecto.precio,
			"item_name" : objecto.nombre,
			"quantity":1,
			"return" : request.build_absolute_uri(reverse('recibido')),
			"cancel_return" : request.build_absolute_uri(reverse('home')),
			"custom" : pk,
			"rm":2,
		}
		except Exception:
			objecto = Prenda.objects.get(pk=pk)	
			paypal_dict = {
				"business" : 'qwer_jv16@outlook.com',
				"amount" : objecto.precio,
				"item_name" : objecto.descripcion,
				"quantity":1,
				"return" : request.build_absolute_uri(reverse('recibido')),
				"cancel_return" : request.build_absolute_uri(reverse('home')),
				"custom" : pk,
				"rm":2,
			}
		form = PayPalPaymentsForm(initial=paypal_dict)
		context = {'form':form, 'objecto':objecto, 'cantidad':1}
		return render(request,"packages/detalle.html",context)

@csrf_exempt
def recibido(request):
	if request.method == 'POST':
		var = request.POST.get('custom')
		act = Portada.objects.get(pk=var)
		cant = int(request.POST.get('quantity'))
		n_stc = act.stock-cant
		act2 = Portada.objects.filter(pk=var).update(stock=n_stc)
	return render(request, 'packages/package.html')

def validar(request, pk):
	context = {'objecto':''}
	if request.method == 'GET':
		cantidad = int(request.GET.get('cantidad'))
		objecto = Portada.objects.get(pk=1)
		try:
			objecto = Portada.objects.get(pk=pk)
			paypal_dict = {
			"business" : 'qwer_jv16@outlook.com',
			"amount" : objecto.precio,
			"item_name" : objecto.nombre,
			"quantity":cantidad,
			"return" : request.build_absolute_uri(reverse('recibido')),
			"cancel_return" : request.build_absolute_uri(reverse('home')),
			"custom" : pk,
			"rm":2,
		}
		except Exception:
			objecto = Prenda.objects.get(pk=pk)	
			paypal_dict = {
				"business" : 'qwer_jv16@outlook.com',
				"amount" : objecto.precio,
				"item_name" : objecto.descripcion,
				"quantity":cantidad,
				"return" : request.build_absolute_uri(reverse('recibido')),
				"cancel_return" : request.build_absolute_uri(reverse('home')),
				"custom" : pk,
				"rm":2,
			}
		limite = objecto.stock
		form = PayPalPaymentsForm(initial=paypal_dict)
		if cantidad <=0:
			retornar1 = 'Ingrese un número válido de artículos'
			context = {'form':form, 'objecto':objecto, 'cantidad':cantidad, 'retornar1':retornar1}

		elif cantidad > limite:
			retornar2 = 'Solo contamos con ' + str(limite)+' artículos en stock'
			context = {'form':form, 'objecto':objecto, 'cantidad':cantidad, 'retornar2':retornar2}
		else:
			context = {'form':form, 'objecto':objecto, 'cantidad':cantidad}
	return render(request, 'packages/detalle.html',context)
    
