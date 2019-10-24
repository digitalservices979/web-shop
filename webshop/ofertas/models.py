from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Ofertas(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    descripcion = RichTextField()
    destinatarios = models.IntegerField()
    fecha_envio = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ofertas'
        ordering =['-fecha_envio']
        verbose_name_plural='Ofertas'

    def __str__(self):
    	return self.titulo