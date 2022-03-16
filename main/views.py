from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def home(request):

    return render(request, 'main/home.html')#! Renderizando el home

def ranking(request):
    return render(request,'main/ranking.html')