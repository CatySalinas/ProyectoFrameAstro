# Generated by Django 5.0.4 on 2024-06-06 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_articulo_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='Articulo/'),
        ),
    ]
