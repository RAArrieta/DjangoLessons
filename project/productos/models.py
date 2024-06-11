from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50, verbose_name="Producto")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio Unitario")
    precio_doc=models.IntegerField(blank=True, null=True, verbose_name="Precio por docena")
    precio_media=models.IntegerField(blank=True, null=True, verbose_name="Precio por mitad")
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    numero=models.IntegerField(verbose_name="Número de Pedido") 
    fecha=models.DateField(verbose_name="Fecha")
    
    def __str__(self):
        return f"{self.numero}"