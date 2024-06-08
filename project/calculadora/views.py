from django.shortcuts import render
from . import funciones

def home(request):
    resultado = None  
    if request.method == 'POST':
        a = int(request.POST.get('a', 0))  
        b = int(request.POST.get('b', 0))  
        if 'sumar' in request.POST:
            resultado = funciones.sumar(a, b)
            return render(request, "calculadora/index.html", {'resultado': resultado})
        if 'restar' in request.POST:
            resultado = funciones.restar(a, b)
            return render(request, "calculadora/index.html", {'resultado': resultado})
        if 'multiplicar' in request.POST:
            resultado = funciones.multiplicar(a, b)
            return render(request, "calculadora/index.html", {'resultado': resultado})
        if 'dividir' in request.POST:
            resultado = funciones.dividir(a, b)
            return render(request, "calculadora/index.html", {'resultado': resultado})
        
    return render(request, "calculadora/index.html", {'resultado': resultado})