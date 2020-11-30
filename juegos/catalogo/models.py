from django.db import models
from django.urls import reverse
import uuid

# Create your models here.


class Game(models.Model):
    cod = models.CharField(max_length=8,primary_key=True)
    nombre = models.CharField(max_length=100)
    creador = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    



    def get_absolute_url(self):
	    return reverse('game_detail', args=[int(self.cod)])


class Usuario(models.Model):
    rut = models.CharField(max_length=8, primary_key=True, help_text="Ingrese rut sin dígito verificador.")
    correo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)


    def __str__(self):
        return self.usuario


    def get_absolute_url(self):
        return reverse('usuario_detail', args=[int(self.rut)])