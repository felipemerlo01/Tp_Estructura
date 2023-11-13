import sys
import os
from Funciones_extra import *
from Hotel import Hotel
from Funciones_lectores import leer_Usuarios, leer_Habitaciones, leer_Reservas
from datetime import datetime
from queue import LifoQueue
from Cliente import Cliente
from Usuario import Usuario

# path='Bases de datos/'
# POO = Hotel('Patagonia: Oasis y Ocio')
# leer_Habitaciones(path+'db_Habitaciones.csv', POO)
# leer_Reservas(path+'db_Reservas.csv', POO)
# leer_Usuarios(path+'db_Usuarios.csv', POO)


    
# Cliente_ej= POO.usuarios['esteban.serrano@gmail.com']

# print(Cliente_ej.reservas)

#Cliente_ej.hacer_reserva(POO)

#POO.actualizar_base_reservas(path+'ReservasPrueba.csv')


# reservas_activas = Cliente_ej.buscar_reservas_activas()
# if (len(reservas_activas) > 0):
#     reserva = Cliente_ej.elegir_habitacion_activa(reservas_activas)
    
#     opciones_comida = {
#     'Desayuno': {'Huevos con tostadas': 900, 'Sandwhich': 1200, 'Cereales': 600},
#     'Bebida': {'Agua': 600, 'Jugo': 700, 'Café': 800},
#     'Refrigerio': {'Barrita': 300, 'Fruta': 300, 'Yogur': 500, 'Galleta': 400}}

#     # 1) Crear pila con elecciones de buffet: tiene que elegir un desayuno, bebida, refrigerio en orden
#     elecciones_comida = LifoQueue()
    
#     for categoria, opciones in opciones_comida.items():
#         print(f'Opciones de {categoria}:')
#         for opcion, precio in opciones.items():
#             print(f'{opcion}: {precio} pesos')
        
#         preferencia = validar_opcion(input(f'Eliga una opcion de {categoria.lower()}: ').capitalize(), opciones)
#         eleccion = (preferencia, opciones[preferencia])
#         elecciones_comida.put(eleccion)
    
#     gastos = 0
#     elementos_orden = []
#     while not elecciones_comida.empty():
#         elemento = elecciones_comida.get()
#         elementos_orden.append(elemento)
#         gastos += elemento[1]
#     reserva.gastos_buffet += gastos
#     # Le muestro su orden
#     orden = ', '.join([f'{elemento[0]} (${elemento[1]})' for elemento in elementos_orden])
#     print(f'Su orden de: {orden} fue efectuada correctamente')
    
    
#     # 2) asigno un empleado random de limpieza que haga limpieza en el buffet
#     admin = POO.buscar_empleado(1)
#     empleado = admin.asignar_empleado_menos_ocupado(POO.usuarios, 'Limpieza')
#     empleado.agregar_tarea_automatica(reserva.habitacion.numero, True)

#     print(empleado.tareas)
#     print(Cliente_ej.reservas[0].gastos_buffet)
# else:
#     print('No esta permitido ir al buffet ya que no está hospedado en el hotel actualmente')

# print()

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
