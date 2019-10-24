from django.db import models

# Create your models here.

class Portada(models.Model):
	cod_portada = models.AutoField(primary_key=True)
	imagen = models.ImageField(upload_to='projects')
	nombre = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	stock = models.IntegerField(blank=True, null=True)

	class Meta:
		verbose_name='Fotos del inicio'
		verbose_name_plural = 'Fotos del inicio'
		db_table = 'portada'

	def __str__(self):
		return self.nombre