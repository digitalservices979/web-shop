from django.db import models

# Create your models here.

class Prenda(models.Model):
    cod_prenda = models.AutoField(primary_key=True)
    stock = models.SmallIntegerField(blank=True, null=True)
    talla = models.CharField(max_length=20, blank=True, null=True)
    imagen_url = models.ImageField(upload_to='projects')
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
    	verbose_name_plural = 'Prendas'
    	db_table = 'prenda'

    def __str__(self):
    	return self.descripcion