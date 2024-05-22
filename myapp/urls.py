from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home),  # Asignando la vista 'home' a la ruta '/home/'
    path('new-design/', views.newDesing),  # Asignando la vista 'newDesign' a la ruta '/new-design/'
    path('car-shop/', views.carShop),  # Asignando la vista 'carShop' a la ruta '/car-shop/'
    path('homeIniciado/',views.homeIniciado), # Asignando la vista 'home
    path('nuevoDiseno/',views.nuevoDiseno), # Asignando la vista 'nuevoDiseno' a la ruta '/nuevoDiseno/'
    path('cuentaUsuario/',views.cuentaUsuario),
    path('contactanos/',views.contactanos),
    path('editarUsuario/',views.editarUsuario)
]
