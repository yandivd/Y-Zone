from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Duelista(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='duelistas')
    ptos=models.IntegerField()
    torneos_clasificados=models.IntegerField()
    torneos_ganados=models.IntegerField()
    id_user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    mensaje=models.TextField()

    def __str__(self):
        return self.nombre

class Torneo_Local(models.Model):
    Primer_Lugar=models.CharField(max_length=50)
    Segundo_Lugar=models.CharField(max_length=50)
    Tercer_Lugar=models.CharField(max_length=50)
    Cuarto_Lugar=models.CharField(max_length=50)
    Quinto_Lugar=models.CharField(max_length=50, blank=True, null=True)
    Sexto_Lugar=models.CharField(max_length=50, blank=True, null=True)
    Septimo_Lugar=models.CharField(max_length=50, blank=True, null=True)
    Octavo_Lugar=models.CharField(max_length=50, blank=True, null=True)

