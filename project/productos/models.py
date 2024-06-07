from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    
    def __str__(self):
        return self.nombre

    
    