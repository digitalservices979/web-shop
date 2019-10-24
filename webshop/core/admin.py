from django.contrib import admin
from .models import Mensajes, Subscriptores
# Register your models here.
class MensajeAdmin(admin.ModelAdmin):
	readonly_fields = ('nombre','fecha_recibido','correo','telefono','asunto',)

admin.site.register(Mensajes, MensajeAdmin)


class SubscriptorAdmin(admin.ModelAdmin):
	readonly_fields = ('correo','fecha_subscripcion',)

admin.site.register(Subscriptores,SubscriptorAdmin)