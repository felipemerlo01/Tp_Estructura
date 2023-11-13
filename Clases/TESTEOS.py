import sys
import os
from Funciones_extra import *
from Hotel import Hotel
from Funciones_lectores import leer_Usuarios, leer_Habitaciones, leer_Reservas
from datetime import datetime


path='Bases de datos/'
POO = Hotel('Patagonia: Oasis y Ocio')
leer_Usuarios(path+'db_Usuarios.csv', POO)
leer_Habitaciones(path+'db_Habitaciones.csv', POO)
leer_Reservas(path+'db_Reservas.csv', POO)
    
POO.crear_informe_estadistico()   


'''
MacBook-Air-de-Camilo:TP Grupo 5 camilobarbero$ python3 "/Users/camilobarbero/Documents/ITBA/2Q2023/Estructura de Datos y Programación/TP Grupo 5/Tp_Estructura-1/TESTEOS.py"
Traceback (most recent call last):
  File "/Users/camilobarbero/Documents/ITBA/2Q2023/Estructura de Datos y Programación/TP Grupo 5/Tp_Estructura-1/TESTEOS.py", line 1, in <module>
    from Clases.Cliente import Cliente
  File "/Users/camilobarbero/Documents/ITBA/2Q2023/Estructura de Datos y Programación/TP Grupo 5/Tp_Estructura-1/Clases/Cliente.py", line 1, in <module>
    from Usuario import Usuario
ModuleNotFoundError: No module named 'Usuario'
'''




""" hotel = Hotel("POO")

habitacion101 = Habitacion(
    numero=101,
    precio=100,  # Reemplaza con el precio real
    capacidad=2,  # Reemplaza con la capacidad real
    tipo="Estándar",  # Reemplaza con el tipo real
    banio_privado="Sí",  # Reemplaza con "Sí" o "No" según corresponda
    balcon="No",  # Reemplaza con "Sí" o "No" según corresponda
)

nueva_reserva = Reserva(
    mail_usuario="nuevo_usuario@gmail.com",
    habitacion=101,
    check_in="10/12/2024",
    check_out="15/12/2024",
) """

#actualizar_base_reservas(nueva_reserva)
