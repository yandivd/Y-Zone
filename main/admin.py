from django.contrib import admin
from .models import Duelista

class DuelistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ptos', 'torneos_jugados', 'torneos_ganados')
    search_fields = ('nombre',)

# Register your models here.
admin.site.register(Duelista, DuelistaAdmin)
