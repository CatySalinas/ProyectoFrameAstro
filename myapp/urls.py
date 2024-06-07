from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('newDesing/', views.newDesing, name='newDesing'),
    path('index/', views.index, name='index'),
    path('carShop/', views.carShop, name='carShop'),
    path('homeIniciado/', views.homeIniciado, name='homeIniciado'),
    path('nuevoDiseno/', views.nuevoDiseno, name='nuevoDiseno'),
    path('cuentaUsuario/', views.cuentaUsuario, name='cuentaUsuario'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('editarUsuario/', views.editarUsuario, name='editarUsuario'),
    path('agregarProducto/', views.agregarProducto, name='agregarProducto'),
    path('datosPago/', views.datosPago, name='datosPago'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('registroUsuario/', views.registroUsuario, name='registroUsuario'),
    path('seguimientoPedido/', views.seguimientoPedido, name='seguimientoPedido'),
    path('compra/', views.compra, name='compra'),
    path('verProducto/', views.verProducto, name='verProducto'),
    path('formulario/', views.formulario, name='formulario'),

    path('base/', views.base),
    path('registrarArticulo/', views.registrarArticulo),
    path('edicionArticulo/<nombre>', views.edicionArticulo),
    path('editarArticulo/', views.editarArticulo),
    path('eliminarArticulo/<nombre>', views.eliminarArticulo)
]
