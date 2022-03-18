from django.shortcuts import render
from django.http import HttpResponse
from .models import Duelista

# Create your views here
def home(request):

    return render(request, 'main/home.html')#! Renderizando el home

def ranking(request):

    data=Duelista.objects.all().order_by("-ptos")
    return render(request, 'main/ranking.html',{"data":data})