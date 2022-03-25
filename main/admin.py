from django.contrib import admin
from .models import Duelista, Contacto, Carta, Ruling

class DuelistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ptos', 'torneos_clasificados', 'torneos_ganados')
    search_fields = ('nombre',)

class ContactoAdmin(admin.ModelAdmin):
    list_display =  ('nombre', 'correo')

class CartaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class RulingAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('cartas',)


# Register your models here.
admin.site.register(Duelista, DuelistaAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Carta)
admin.site.register(Ruling, RulingAdmin)
