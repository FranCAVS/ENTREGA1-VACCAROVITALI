from django import forms

class AutosBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class FormularioLicencias(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()