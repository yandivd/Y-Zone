from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Duelista(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='duelistas')
    ptos=models.FloatField()
    torneos_jugados=models.IntegerField()
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

