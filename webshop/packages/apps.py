from django.apps import AppConfig

class PackagesConfig(AppConfig):
    name = 'packages'
    verbose_name = 'Agregar Prendas'

    def ready(self):
    	from paypal.standard.models import ST_PP_COMPLETED
    	from paypal.standard.ipn.signals import valid_ipn_received




