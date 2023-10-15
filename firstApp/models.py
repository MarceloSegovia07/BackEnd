from django.db import models

# Create your models here.
class Employee(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fono = models.CharField(max_length=15)


class Importacion(models.Model):
    NombreArticulo= models.CharField(max_length=40)
    NombreProveedor=models.CharField(max_length= 40)
    CodigoArticulo= models.CharField(max_length=30)
    TotalPedidoCLP= models.IntegerField()
    CostoEnvioCLP= models.IntegerField()
    AduanaCLP= models.IntegerField()
    IVAclp = models.IntegerField()
    AduanaMasIVACLP= models.IntegerField()
    CostoTotalCLP = models.IntegerField()
    CostoTotalUSD = models.IntegerField()

