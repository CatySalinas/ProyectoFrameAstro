from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10,  default='')
    direccion = models.CharField(max_length=100, default='')
    correo=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=100)


class cuentaUsuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)



    def _str_(self):
        return f'{self.nombre} {self.apellidos}'
    


class ProductMaterial(models.Model):
    name = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product_material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        ordering= ['id']	

class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre')
    category = models.ForeignKey(ProductMaterial, on_delete=models.CASCADE,verbose_name='Material')
    image= models.ImageField(upload_to='products/', null=True, blank=True,verbose_name='Imagen')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Precio')
    details = models.TextField(max_length=500,verbose_name='Descripción')
   
   
def __str__(self):
    return self.name

class meta:
    db_table = 'products'
    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'
    ordering = ['id']





class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    material = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    """imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)  # Agregar esta línea"""

    def _str_(self):

        return self.nombre

class CarritoDeCompras(models.Model):
    articulos = models.ManyToManyField(Articulo)
    #esto es para enlazar la informacion de usuario con la de carrito de compras
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def _str_(self):
        return f'Carrito de compras {self.id}'


class Compra(models.Model):
    ESTADOS_DE_COMPRA = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    articulos = models.ManyToManyField(Articulo)
    cantidad = models.PositiveIntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADOS_DE_COMPRA, default='Pendiente')
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'Compra de {", ".join([articulo.nombre for articulo in self.articulos.all()])} por {self.usuario.nombre} ({self.estado})'

