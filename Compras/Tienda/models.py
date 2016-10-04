from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
	nombre = models.CharField(max_length=140,null=True,blank=True)
	precio = models.FloatField(null=True,blank=True)
	descripcion = models.CharField(max_length=140,null=True,blank=True)
	imagen = models.ImageField(upload_to="files",blank=True,null=True)
	categorita = models.CharField(max_length=140,null=True,blank= True)