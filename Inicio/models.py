from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    #contraseña = models.CharField(max_length=8)
    
    #agregar campos segun necesidad

