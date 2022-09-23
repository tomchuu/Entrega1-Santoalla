from django.db import models

# Create your models here.

class Gimnasio(models.Model):
    
    nombre = models.CharField(max_length=60)
    valoracion = models.IntegerField()



class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fechadeingreso = models.DateTimeField()



class Rutinas(models.Model):
    nombre = models.CharField(max_length=60)
    dias = models.DateTimeField()
