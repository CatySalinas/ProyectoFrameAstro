from django.urls import path
from . import views 
from .views import user_login
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

    #path('accounts/',include('django.contrib.auth.urls'))
     path('login/', user_login, name='login')

    path('compra',views.compra),
    path('verProducto/',views.verProducto),

]
