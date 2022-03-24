from django import forms
from .models import Contacto, Torneo_Local

class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contacto
        fields='__all__'

class TorneoLocalForm(forms.ModelForm):

    class Meta:
        model=Torneo_Local
        fields='__all__'