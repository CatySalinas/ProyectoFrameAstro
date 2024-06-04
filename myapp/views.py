from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # Redirige a la página de inicio después del login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


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
