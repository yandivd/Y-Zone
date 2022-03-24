from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Duelista
from .forms import ContactoForm, ResultadosForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

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

@permission_required('main.change_duelista')
def actualizar_resultados(request):
    #####Falta validar q no se llenen todos los campos
    #### y q no me devuelva un objeto vacio

    data = {
        "form": ResultadosForm()
    }

    if request.method=='POST':
        formulario=ResultadosForm(data=request.POST)

        if formulario.is_valid():

            #guardar los 8 jugadores q cogen puntos cada uno en una variable
            p1=formulario.cleaned_data["Primer_Lugar"]
            p2=formulario.cleaned_data["Segundo_Lugar"]
            p3=formulario.cleaned_data["Tercer_Lugar"]
            p4=formulario.cleaned_data["Cuarto_Lugar"]
            p5=formulario.cleaned_data["Quinto_Lugar"]
            p6=formulario.cleaned_data["Sexto_Lugar"]
            p7=formulario.cleaned_data["Septimo_Lugar"]
            p8=formulario.cleaned_data["Octavo_Lugar"]

            #actualizar los puntos para cada jugador
            lista_jug=[]
            lista_jug_no_oblig=[]
            try:
                jugador=Duelista.objects.get(nombre=p1)
                jugador.ptos+=8
                jugador.torneos_ganados+=1
                jugador.torneos_clasificados+=1
                lista_jug.append(jugador)

                jugador=Duelista.objects.get(nombre=p2)
                jugador.ptos+=7
                jugador.torneos_clasificados += 1
                lista_jug.append(jugador)

                jugador = Duelista.objects.get(nombre=p3)
                jugador.ptos += 6
                jugador.torneos_clasificados += 1
                lista_jug.append(jugador)

                jugador = Duelista.objects.get(nombre=p4)
                jugador.ptos += 5
                jugador.torneos_clasificados += 1
                lista_jug.append(jugador)
            except:
                data["form"] = formulario
                messages.error(request,"Usuario Incorrecto")
                return render(request, 'resultados/actualizar.html', data)




            if p5==None:
                for i in lista_jug:
                    i.save()
                return redirect(to=ranking)
            else:
                try:
                    jugador = Duelista.objects.get(nombre=p5)
                    jugador.ptos += 4
                    jugador.torneos_clasificados += 1
                    lista_jug_no_oblig.append(jugador)

                except:
                    data["form"] = formulario
                    messages.error(request, "Usuario Incorrecto")
                    return render(request, 'resultados/actualizar.html', data)

            if p6==None:
                for i in lista_jug:
                    i.save()
                for i in lista_jug_no_oblig:
                    i.save()
                return redirect(to=ranking)
            else:
                try:
                    jugador = Duelista.objects.get(nombre=p6)
                    jugador.ptos += 3
                    jugador.torneos_clasificados += 1
                    lista_jug_no_oblig.append(jugador)

                except:
                    data["form"] = formulario
                    messages.error(request, "Usuario Incorrecto")
                    return render(request, 'resultados/actualizar.html', data)

            if p7==None:
                for i in lista_jug:
                    i.save()
                for i in lista_jug_no_oblig:
                    i.save()
                return redirect(to=ranking)
            else:
                try:
                    jugador = Duelista.objects.get(nombre=p7)
                    jugador.ptos += 2
                    jugador.torneos_clasificados += 1
                    lista_jug_no_oblig.append(jugador)

                except:
                    data["form"] = formulario
                    messages.error(request, "Usuario Incorrecto")
                    return render(request, 'resultados/actualizar.html', data)

            if p8==None:
                for i in lista_jug:
                    i.save()
                for i in lista_jug_no_oblig:
                    i.save()
                return redirect(to=ranking)
            else:
                try:
                    jugador = Duelista.objects.get(nombre=p8)
                    jugador.ptos += 1
                    jugador.torneos_clasificados += 1
                    lista_jug_no_oblig.append(jugador)

                except:
                    data["form"] = formulario
                    messages.error(request, "Usuario Incorrecto")
                    return render(request, 'resultados/actualizar.html', data)

            for i in lista_jug:
                i.save()
            for i in lista_jug_no_oblig:
                i.save()

            return redirect('ranking')
    return render(request, 'resultados/actualizar.html', data)

def reiniciar_ranking(request):

    lista_duelistas=Duelista.objects.all()
    for i in lista_duelistas:
        i.ptos=0
        i.torneos_ganados=0
        i.torneos_clasificados=0
        i.save()
        messages.success(request,"Ranking Reiniciado")

    return redirect(to='home')

