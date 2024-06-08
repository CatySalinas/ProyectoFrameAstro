from django.shortcuts import render, redirect 
from django.http import HttpResponse
from . forms import UsuarioForm
from django.db.models import Q
from .forms import ProductForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Product
from django.db import IntegrityError
from .models import Articulo
from django.contrib import messages
from .forms import ProductMaterialForm
# Create your views here.

def about(request):
    return HttpResponse("<h1>About Us<h1>")

def home(request):
    return render(request, 'home.html')

def newDesing(request):
    return HttpResponse("<h1>New Desing Page<h1>")

def index(request):
    return render(request, 'index.html')

def carShop(request):
    return render(request, 'carShop.html')


def homeIniciado(request):
    return render(request, 'homeIniciado.html')



def nuevoDiseno(request):
    return render(request, 'nuevoDiseno.html')

def cuentaUsuario(request):
    return render(request, 'cuentaUsuario.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def editarUsuario(request):
    return render(request, 'editarUsuario.html')

def agregarProducto(request):
    return render(request, 'agregarProducto.html')

def datosPago(request):
    return render(request, 'datosPago.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def registroUsuario(request):
    return render(request, 'registroUsuario.html')

def seguimientoPedido(request):
    return render(request, 'seguimientoPedido.html')

def compra(request):
    return render(request, 'compra.html')


def verProducto(request):
    return render(request, 'verProducto.html')

def politicas(request):
    return render(request, 'politicas.html')


def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm(),
                    "error": "El usuario ya existe"
                })

        return render(request, 'registro.html', {
                    'form': UserCreationForm(),
                    "error": "Las contraseñas no coinciden"
                })
def cerrarSesion(request):
        logout(request)
        return redirect('home')
    
def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'inicioSesion.html',{
        'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
              return render(request, 'inicioSesion.html',{
                 'form': AuthenticationForm,
                 'error': 'Usuario o contraseña son incorrectos'
                })
        else:
            login(request, user)
            return redirect('home')
            
    
        
    

def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request, 'formulario.html', {'form': form})

def buscador(request):
    busqueda = request.POST.get('buscar')
    articulo= Articulo.objects.all()
    if busqueda:
        articulo= Articulo.objects.filter(
            Q(nombre__iconstains=busqueda)| 
            Q(categoria__iconstains=busqueda)|
            Q(
               material__iconstains=busqueda 
            )
        ).distinct()
        return(render(request,'articulo.html',{articulo:articulo}))




def base(request):
    articulo = Articulo.objects.all()
    messages.success(request, '¡Articulo listados!')
    return render(request, "gestionInventario.html", {"articulo": articulo})

def registrarArticulo(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    material = request.POST['txtMaterial']
    costo = request.POST['numCosto']
   


    articulo = Articulo.objects.create(
    nombre=nombre, categoria=categoria, descripcion=descripcion, material=material, costo=costo)
    messages.success(request, '¡Articulo registrado!')
    return redirect("http://127.0.0.1:8000/base/")



def edicionArticulo(request, nombre):
    articulo = Articulo.objects.get (nombre=nombre)
    return render(request, "edicionInventario.html", {"articulo": articulo})


def editarArticulo(request):
    nombre = request.POST['txtNombre']
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    material = request.POST['txtMaterial']
    costo = request.POST['numCosto']
   

    articulo = Articulo.objects.get(nombre=nombre)
    articulo.nombre=nombre, 
    articulo.categoria=categoria, 
    articulo.descripcion=descripcion,
    articulo.material=material, 
    articulo.costo=costo
    articulo.save()

    messages.success(request, '¡Articulo actualizado!')
    return redirect("http://127.0.0.1:8000/base/")


def eliminarArticulo(request, nombre):
    articulo = Articulo.objects.get(nombre=nombre)
    articulo.delete()
    messages.success(request, '¡Articulo eliminado!')
    return redirect("http://127.0.0.1:8000/base/")    


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../add-product')  # Redirect to a list of products or any other page
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def add_material(request):
    if request.method == 'POST':
        form = ProductMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../add-material')  # Redirect to a list view or another relevant page
    else:
        form = ProductMaterialForm()

    return render(request, 'add_material.html', {'form': form})

def home (request):
    productos = Product.objects.all()
    return render(request, 'home.html', {'productos': productos})


