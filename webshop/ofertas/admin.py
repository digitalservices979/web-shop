from django.contrib import admin
from django.urls import path,reverse_lazy
from django.template.response import TemplateResponse
from .models import Ofertas
from .forms import OfertaForm
from django.views.generic.edit import CreateView

# Register your models here.

class OfertasAdmin(admin.ModelAdmin):
	readonly_fields = ('titulo','asunto','descripcion','destinatarios','fecha_envio',)

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [ path('add/', self.admin_site.admin_view(OfertaCreateView.as_view())),]
		return my_urls + urls


class OfertaCreateView(CreateView):
	model = Ofertas
	form_class = OfertaForm
	template_name = "ofertas/email_ofertas.html"
	success_url = reverse_lazy('confirmacion')

admin.site.register(Ofertas,OfertasAdmin)