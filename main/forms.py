from django import forms
from .models import Contacto, Torneo_Local, Carta, Ruling

class ContactoForm(forms.ModelForm):

    class Meta:
        model=Contacto
        fields='__all__'

class ResultadosForm(forms.ModelForm):

    class Meta:
        model=Torneo_Local
        fields='__all__'

class CartaForm(forms.ModelForm):

    class Meta:
        model=Carta
        fields='__all__'

class RulingForm(forms.ModelForm):

    class Meta:
        model=Ruling
        fields='__all__'