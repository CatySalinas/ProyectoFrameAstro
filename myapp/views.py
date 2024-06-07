from django.shortcuts import render, redirect 
from django.http import HttpResponse
from . forms import UsuarioForm
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here

def about(request):
    return HttpResponse("<h1>About Us<h1>")

def home(request):
    return render(request, 'home.html')

def newDesing(request):
    return HttpResponse("<h1>New Desing Page<h1>")

def index(request):
    return render(request, 'index.html')

def carShop(request):
    return HttpResponse("<h1>Card Page<h1>")


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


def carShop(request):
    return render(request, 'carShop.html')


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
            
    
        
    