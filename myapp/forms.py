from django import forms
from . models import Usuario
from .models import Product
from .models import ProductMaterial
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario 
        fields = ['nombre', 'apellidos', 'correo','telefono','direccion', 'contraseña']

class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'price', 'details']  
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'
            }),
            'category': forms.Select(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'
            }),
            'details': forms.Textarea(attrs={
                'class': 'block w-full h-32 px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring',
                'rows': 4,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mt-2'
            }),
        }

class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ['name', 'featured']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring'
            }),
            'featured': forms.CheckboxInput(attrs={
                'class': 'mt-2'
            }),
        }