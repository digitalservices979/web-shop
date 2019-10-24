from django.urls import path
from .views import enviando

urlpatterns = [
	path('confirmacion/', enviando, name='confirmacion'),
]