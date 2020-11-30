from django import forms



class GameForm(forms.Form):
    cod = forms.CharField()
    nombre = forms.CharField()
    creador = forms.CharField()
    descripcion = forms.CharField()