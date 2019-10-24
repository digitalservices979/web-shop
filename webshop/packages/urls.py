from django.urls import path
from .views import *

urlpatterns = [
	path('articulos/', PackageListView.as_view(), name='package'),
	path('detallar/<int:pk>/', PrendaDetailView.as_view(), name='detallar'),
	path('gracias', recibido, name='recibido'),
	path('validar/<int:pk>/', validar, name='validar'),
]