from django.shortcuts import render
from . import funciones

# Create your views here.
def home(request):
    resultado = None  # Define un valor por defecto para resultado
    if request.method == 'POST':
        a = int(request.POST.get('a', 0))  # Obtén el valor de 'a' y conviértelo a entero
        b = int(request.POST.get('b', 0))  # Obtén el valor de 'b' y conviértelo a entero
        resultado = funciones.sumar(a, b)
        
    return render(request, "calculadora/index.html", {'resultado': resultado})