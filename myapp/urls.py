from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('new-design/', views.newDesing, name='new-design'),
    path('carShop/', views.carShop, name='car-shop'),
    path('homeIniciado/', views.homeIniciado, name='home-iniciado'),
    path('nuevoDiseno/', views.nuevoDiseno, name='nuevo-diseno'),
    path('cuentaUsuario/', views.cuentaUsuario, name='cuenta-usuario'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('editarUsuario/', views.editarUsuario, name='editar-usuario'),
    path('agregarProducto/', views.agregarProducto, name='agregar-producto'),
    path('datosPago/', views.datosPago, name='datos-pago'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('registroUsuario/', views.registroUsuario, name='registro-usuario'),
    path('seguimientoPedido/', views.seguimientoPedido, name='seguimiento-pedido'),
    path('carShop/', views.carShop, name='car-shop'),
    path('login/', LoginView.as_view(template_name='homeIniciado.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('compra', views.compra, name='compra'),
    path('verProducto/', views.verProducto, name='ver-producto'),
    path('politicas/', views.politicas, name='politicas'),
    path('registro/', views.registro, name='registro'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrar-sesion'),
    path('inicioSesion/', views.inicioSesion, name='inicio-sesion'),
]
