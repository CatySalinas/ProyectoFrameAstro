from django import forms
from . models import Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario 
        fields = ['nombre', 'apellidos', 'correo','telefono','direccion', 'contraseña']