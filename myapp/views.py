from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def hello (request):
    return HttpResponse("<h1>Hello World<h1>")

def about (request):
    return HttpResponse("<h1>About Us<h1>")

def home (request):
    return render(request,'home.html')

def newDesing (request):
    return HttpResponse("<h1>New Desing Page<h1>")

def carShop (request):
    return HttpResponse("<h1>Card Page<h1>")
def homeIniciado(request):
    return render(request,'homeIniciado.html')
def nuevoDiseno(request):
    return render(request,'nuevoDiseno.html')
def cuentaUsuario(request):
    return render(request, 'cuentaUsuario.html')
def contactanos(request):
    return render(request, 'contactanos.html')
def editarUsuario(request):
    return render(request, 'editarUsuario.html')