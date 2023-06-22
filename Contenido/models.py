from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
	tipoProducto = models.CharField(primary_key=True, max_length=3, verbose_name="tipoProducto")
	nombreTipo = models.CharField(max_length=50, verbose_name="nombreTipo")
	
	def __str__(self):
		return self.nombreTipo

class Plantita(models.Model):
	idProducto = models.CharField(primary_key=True, max_length=4, verbose_name="idProducto")
	tituloProducto = models.CharField(max_length=50, verbose_name="tituloProducto")
	precio = models.IntegerField(verbose_name="precio")
	descripcion = models.CharField(max_length=300, verbose_name="descripcion")
	imagen=models.ImageField(upload_to="imagenes",null=True, blank=True,verbose_name="Imagen")
	Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="categoriaProduct")

	def __str__(self):
		return self.tituloProducto