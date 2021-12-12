from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tienda/', views.tienda, name='tienda'),
#    path('login/', views.login, name='login'),


]