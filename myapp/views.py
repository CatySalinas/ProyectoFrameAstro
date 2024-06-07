from django.shortcuts import render, redirect
from django.http import HttpResponse



from . forms import UsuarioForm

from django.db.models import Q
from django.shortcuts import render

from .models import Articulo
from django.contrib import messages


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

