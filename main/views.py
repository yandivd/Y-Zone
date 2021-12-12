from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def home(request):

    #* Aqui por ahora no necesito que me mandes nada.
    #! Encargate de la rpoteccion de urls!!!!!!!


    return render(request, 'home.html')#! Renderizando el home 

def tienda(request):

    return HttpResponse('Tienda')

#def login(request):
#    return render(request,'registration/login.html')