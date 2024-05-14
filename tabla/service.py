from .models import Chofer, Vehiculo, RegistroContabilidad
from datetime import date


def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save()


def crear_chofer(rut, nombre, apellido, creacion_registro):
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, creacion_registro=creacion_registro)
    chofer.save()


def crear_registro_contable(fecha_compra, valor, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    registro = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    registro.save()


def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()


def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()


def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()


def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = True
    vehiculo.save()


def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return vehiculo


def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer


def asignar_chofer_a_vehiculo(rut, patente):
    chofer = Chofer.objects.get(rut=rut)
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.chofer = chofer
    vehiculo.save()


def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}")
