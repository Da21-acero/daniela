from django.db import models

# Create your models here.

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    duracion= models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(slef):
        return self.nombre