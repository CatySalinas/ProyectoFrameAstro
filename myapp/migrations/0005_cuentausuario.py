# Generated by Django 5.0.4 on 2024-06-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_articulo_usuario_carritodecompras_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuentaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]