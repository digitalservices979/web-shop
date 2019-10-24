from django.db import models

# Create your models here.
class Blog(models.Model):
	cod_blog = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to='projects')
	descripcion = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

	class Meta:
		verbose_name='Blog'
		verbose_name_plural = 'Blogs'
		db_table = 'blog'
		ordering = ['-fecha_creacion']

	def __str__(self):
		return self.titulo