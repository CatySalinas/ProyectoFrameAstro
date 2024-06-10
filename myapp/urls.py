from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_product,add_material,buscador,search_products
from . import views 


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
    path('lista_productos/',buscador),
    path('base/', views.base),
    path('registrarArticulo/', views.registrarArticulo),
    path('edicionArticulo/<nombre>', views.edicionArticulo),
    path('editarArticulo/', views.editarArticulo),
    path('eliminarArticulo/<nombre>', views.eliminarArticulo),
    path('add-material/', add_material, name='add_material'),
     path('search/', search_products, name='search_products'),
    path('add-product/', add_product, name='add_product'),


   path('buscar/', buscador, name='buscador'),

    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('pedidoRealizado/', views.pedidoRealizado, name='pedido-realizado'),
    path('seguimientoPedidoAdmin/', views.seguimientoPedidoAdmin, name='seguimiento-pedido-admin'),
    
  

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
