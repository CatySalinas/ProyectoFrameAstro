from django.shortcuts import render

from django.http import HttpResponse


from . forms import UsuarioForm

from django.db.models import Q
from django.shortcuts import render

# Create your views here.




def about (request):
    return HttpResponse("<h1>About Us<h1>")

def home (request):
    return render(request,'home.html')

def newDesing (request):
    return HttpResponse("<h1>New Desing Page<h1>")
def index (request):
    return render(request,'index.html')
def carShop (request):
    return HttpResponse("<h1>Card Page<h1>")
def homeIniciado(request):
    return render(request,'homeIniciado.html')
def nuevoDiseno(request):
    return render(request,'nuevoDiseno.html')
def carShop(request):
    return render(request,'carShop.html')
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