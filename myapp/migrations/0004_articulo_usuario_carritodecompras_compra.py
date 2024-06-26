
# Generated by Django 5.0.6 on 2024-06-03 03:59


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('material', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),

                ('imagen', models.ImageField(blank=True, null=True, upload_to='articulos/')),

            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoDeCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulos', models.ManyToManyField(to='myapp.articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], default='Pendiente', max_length=20)),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('articulos', models.ManyToManyField(to='myapp.articulo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario')),
            ],
        ),
    ]
