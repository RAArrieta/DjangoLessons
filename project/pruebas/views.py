from django.shortcuts import render

# Create your views here.

def home(request):
    enviar_lista
    return render(request, "pruebas/index.html")

def enviar_lista(request):
    lista=[0,1,2,3,4,5]
    return render(request, "pruebas/components/lista.html", {'lista': lista})