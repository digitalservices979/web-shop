from django.shortcuts import render
from core.models import Subscriptores
from .models import Ofertas
from django.conf import settings
from django.core import mail

# Create your views here.

def enviando(request, **kwargs):
	Mensaje_a_enviar = Ofertas.objects.latest('id_oferta')
	destinos = Subscriptores.objects.all()
	coneccion = mail.get_connection()
	coneccion.open()
	lista_correos = []
	for ob in destinos:
		lista_correos.append(ob.correo)

	lista_emails=[]
	a=0
	for i in lista_correos:

		lista_emails.append(
				mail.EmailMessage(
						Mensaje_a_enviar.asunto,
						Mensaje_a_enviar.descripcion,
						settings.EMAIL_HOST_USER,
						to=[lista_correos[a]],
					)
			)
		a = a+1
	coneccion.send_messages(lista_emails)
	coneccion.close()
	return render(request,'ofertas/confirmacion.html')
