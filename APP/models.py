from django.db import models

# Create your models here.
class Autos(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.IntegerField()

class Motos(models.Model):
    marca= models.CharField(max_length=30)
    modelo = models.IntegerField()

class Licencias(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()