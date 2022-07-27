from email.policy import default
from django.db import models
from sqlalchemy import true
from tables import Description

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    #auto_now_add permitira registrar 
    #la fecha cuando cree el registro
    creado = models.DateTimeField(auto_now_add=True)
    #auto_now me permitira registrar
    #la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

class categoria(models.Model):
    nombre = models.CharField(max_length=110)
    Description = models.CharField(max_length=250)
    #DataField() sirve para guardar la fecha manualmente
    creado = models.DateField()