from Clases.Cliente import Cliente
from Clases.Empleado import Empleado
from Clases.Funciones_extra import *
from Clases.Reserva import Reserva

# Testear cosas por acá
def actualizar_base_reservas(reserva):
    info_reserva = f"{reserva.mail_usuario},{reserva.habitacion.numero},{reserva.check_in},{reserva.check_out}\n"
    with open("D:\Downloads\Estructura de datos y programacion\TP\Tp_Estructura\Bases de datos\db_Reservas copy.csv","a",newline='') as archivo_reservas:
        archivo_reservas.write(info_reserva)




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
