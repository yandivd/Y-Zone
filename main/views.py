from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Duelista
from .forms import ContactoForm
from django.contrib import messages

# Create your views here
def home(request):

    return render(request, 'main/home.html')#! Renderizando el home

def ranking(request):

    data=Duelista.objects.all().order_by("-ptos")
    return render(request, 'main/ranking.html',{"data":data})

def contacto(request):

    data={
        "form": ContactoForm() #crear una instancia del formulario para enviarlo al template

    }

    if(request.method=='POST'): #verifico si lo q me esta enviando son datos y q el metodo sea post
        formulario=ContactoForm(data=request.POST) #creo un nuevo formulario pero con los datos q estoy enviando
        if formulario.is_valid(): #verifica q el formulario sea valido para guardarlo
            formulario.save()
            #data["mensaje"]="Gracias por Contactarnos" #crea un mensaje y lo agrega al data
            messages.success(request, "Gracias por su comentario")
            return redirect(to='home')
        else:
            data["form"]=formulario #si no es valido reenvia el mismo formulario con los errores

    return render(request, 'main/contacto.html', data)