from collections import defaultdict
from django.shortcuts import render
from productos.models import Producto
from . import funciones

# Create your views here.

def home(request):
    return render(request, "pruebas/index.html")

def enviar_lista(request):
    lista=[0,1,2,3,4,5]
    return render(request, "pruebas/components/lista.html", {'lista':lista})

def select_productos(request):
    categorias=funciones.select_productos()
    producto=None
    cantidad=0
    mensaje=None

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))
        if not producto_id:
            mensaje="Debe seleccionar un producto..."
        else:
            producto = Producto.objects.get(pk=producto_id)
            mensaje=None
 
 
    context = {
        'categorias': categorias,
        'producto':producto,
        'cantidad':cantidad,
        'mensaje':mensaje
    }
    
    return render(request, 'pruebas/components/select_productos/select_productos.html', context)

# def agregar_producto(request):
#     if request.method == 'POST':
#         producto_id = request.POST.get('producto')
#         cantidad = request.POST.get('cantidad')
        
#         # Obtener el objeto Producto correspondiente al producto_id
#         producto = Producto.objects.get(pk=producto_id)
        
#         producto_pedido={
#             'producto':producto,
#             'cantidad':cantidad
#         }
#     return render(request, "pruebas/components/select_productos/select_productos.html",producto_pedido)