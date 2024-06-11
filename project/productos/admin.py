from django.contrib import admin
from .models import CategoriaProducto, Producto, Cliente, Pedido

class ProductoAdmin(admin.ModelAdmin):
    # ORDENO EN ADMIN POR NOMBRE, PRECIO
    list_display=("nombre", "precio", "precio_doc", "precio_media")
    search_fields=("nombre",)
    list_filter=("categoria",)
    
class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    # FILTRAR POR FECHA
    list_filter=("fecha",)
    date_hierarchy="fecha"
    

admin.site.register(CategoriaProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido, PedidoAdmin)