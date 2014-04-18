#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Recet(models.Model):
	titulo=models.CharField(max_length=100, verbose_name='Título', unique=True)
	ingredientes = models.TextField(help_text='agrega los ingredientes')
	preparacion = models.TextField(verbose_name='Preparacion')
	imagen = models.ImageField(upload_to='Imagenes', verbose_name='Imagen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
	receta=models.ForeignKey(Recet)
	texto=models.TextField(help_text='Comentario de prueba',verbose_name='comentario')

	def __unicode__(self):
		return self.texto