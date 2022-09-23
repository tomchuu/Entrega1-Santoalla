from django import forms


class FormularioRutinas(forms.Form):

    nombre = forms.CharField()
    dias = forms.DateField()



class FormularioCliente(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    fechadeingreso = forms.DateField()



class FormularioGimnasio(forms.Form):

    nombre = forms.CharField()
    valoracion = forms.IntegerField()