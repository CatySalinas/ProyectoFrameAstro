from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    
    path('', views.home),  # Asignando la vista 'home' a la ruta '/home/'
    path('new-design/', views.newDesing),  # Asignando la vista 'newDesign' a la ruta '/new-design/'
    path('carShop/', views.carShop),  # Asignando la vista 'carShop' a la ruta '/car-shop/'
    path('homeIniciado/',views.homeIniciado), # Asignando la vista 'home
    path('nuevoDiseno/',views.nuevoDiseno), # Asignando la vista 'nuevoDiseno' a la ruta '/nuevoDiseno/'
    path('cuentaUsuario/',views.cuentaUsuario),
    path('contactanos/',views.contactanos),
    path('editarUsuario/',views.editarUsuario),
    path('agregarProducto/',views.agregarProducto),
    path('datosPago/',views.datosPago),
    path('catalogo',views.catalogo),
    path('registroUsuario/',views.registroUsuario),
    path('seguimientoPedido/',views.seguimientoPedido),
    path('carShop/',views.carShop),
    path('login/', LoginView.as_view(template_name='homeIniciado.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('formulario/',views.formulario,name='formulario'),
    path('compra',views.compra),
    path('verProducto/',views.verProducto),
    path ('formulario/',views.formulario,name='formulario')

]
