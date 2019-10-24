from django.urls import path
from .views import *

urlpatterns = [
	path('about/', AboutTemplateView.as_view(), name='about'),
	path('contact/', ContactTemplateView.as_view(), name='contact'),
	path('contact/mensajes/', mensajes, name='mensajes'),
	path('subscriptores/', subscriptores, name='subscriptores'),
]