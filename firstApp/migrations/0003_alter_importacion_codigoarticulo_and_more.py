# Generated by Django 4.2.4 on 2023-10-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_importacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacion',
            name='CodigoArticulo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='importacion',
            name='NombreArticulo',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='importacion',
            name='NombreProveedor',
            field=models.CharField(max_length=40),
        ),
    ]