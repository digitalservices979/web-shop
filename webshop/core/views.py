from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Mensajes, Subscriptores
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class AboutTemplateView(TemplateView):
	template_name = "core/about.html"

class ContactTemplateView(TemplateView):
	template_name = "core/contact.html"


@csrf_exempt
def mensajes(request):
	if request.is_ajax():
		if request.method == 'POST':
			mensajes = Mensajes()
			obj_json = json.loads(request.POST.get('lista'))
			mensajes.nombre = obj_json["nombre"]
			mensajes.correo = obj_json["correo"]
			mensajes.telefono = obj_json["tel"]
			mensajes.asunto = obj_json["mensaje"]
			mensajes.save()
			lista_devuelta = ["Gracias por comunicarte con nosotros!"]
			return HttpResponse(json.dumps(list(lista_devuelta)), content_type='application/json')
	else:
		return HttpResponse('Solo ajax')

@csrf_exempt
def subscriptores(request):
	if request.is_ajax():
		if request.method == 'POST':
			todos = Subscriptores.objects.all();
			x=0
			lista_devuelta = ["Gracias por subscribirte!"]
			for subs in todos:
				if subs.correo == request.POST.get('correo'):
					lista_devuelta= ["Usted ya está subscrito"]
					x = x+1
			if x==0:
				subscriptor = Subscriptores()
				subscriptor.correo = request.POST.get('correo','Error')
				subscriptor.save()
		return HttpResponse(json.dumps(list(lista_devuelta)), content_type='application/json')
	else:
		return HttpResponse('Solo ajax')