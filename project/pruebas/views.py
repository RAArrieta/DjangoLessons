from collections import defaultdict
from django.shortcuts import render
from productos.models import Producto

# Create your views here.

def home(request):
    enviar_lista
    return render(request, "pruebas/index.html")

def enviar_lista(request):
    lista=[0,1,2,3,4,5]
    return render(request, "pruebas/components/lista.html", {'lista':lista})

def select_productos(request):
    productos = Producto.objects.all()
    categorias = {}
    for producto in productos:
        if producto.categoria not in categorias:
            categorias[producto.categoria] = []
        categorias[producto.categoria].append(producto)
    
    context = {
        'categorias': categorias
    }
    
    return render(request, 'pruebas/components/select_productos.html', context)

def agregar_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        
        # Obtener el objeto Producto correspondiente al producto_id
        producto = Producto.objects.get(pk=producto_id)
        
        # Imprimir el nombre del producto
        print(f"Producto: {producto.nombre}")
        print(f"Cantidad: {cantidad}")
    
    return render(request, "pruebas/components/agregar_producto.html")