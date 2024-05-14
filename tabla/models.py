from django.db import models

from django.db import models


class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField()
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.SET_NULL, null=True, unique=True)


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField()


class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    valor = models.FloatField()
    vehiculo = models.OneToOneField('Vehiculo', on_delete=models.CASCADE, unique=True)
