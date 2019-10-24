from django.urls import path
from .views import PortadaListView

urlpatterns = [
	path('', PortadaListView.as_view(), name='home'),
]