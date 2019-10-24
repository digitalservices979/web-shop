from django.db import models

# Create your models here.
class Mensajes(models.Model):
    cod_mensaje = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_recibido = models.DateTimeField(auto_now=True)
    correo = models.CharField(max_length=200)
    telefono = models.TextField()
    asunto = models.TextField()

    class Meta:
        db_table = 'mensajes'
        ordering = ['-fecha_recibido']
        verbose_name_plural = 'Mensajes'

    def __str__(self):
    	return self.nombre

class Subscriptores(models.Model):
    id_subscriptor = models.AutoField(primary_key=True)
    correo = models.TextField()
    fecha_subscripcion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subscriptores'
        ordering = ['-fecha_subscripcion']
        verbose_name_plural = 'Subscriptores'

    def __str__(self):
        return self.correo