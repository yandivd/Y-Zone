from django.contrib import admin
from .models import Duelista, Contacto

class DuelistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ptos', 'torneos_jugados', 'torneos_ganados')
    search_fields = ('nombre',)

class ContactoAdmin(admin.ModelAdmin):
        list_display =  ('nombre', 'correo')


# Register your models here.
admin.site.register(Duelista, DuelistaAdmin)
admin.site.register(Contacto, ContactoAdmin)
