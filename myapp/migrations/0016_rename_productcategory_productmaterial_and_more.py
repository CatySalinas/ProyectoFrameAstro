# Generated by Django 5.0.4 on 2024-06-07 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_productcategory_carritodecompras_usuario_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='ProductMaterial',
        ),
        migrations.AlterModelOptions(
            name='productmaterial',
            options={'ordering': ['id'], 'verbose_name': 'Material', 'verbose_name_plural': 'Materiales'},
        ),
        migrations.AlterModelTable(
            name='productmaterial',
            table='product_material',
        ),
    ]
