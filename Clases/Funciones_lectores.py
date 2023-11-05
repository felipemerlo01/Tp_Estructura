# Funciones de lectura de las bases de datos: 
from Cliente import Cliente
from Empleado import Empleado
from Administrador import Administrador
from Habitacion import Habitacion
from Reserva import Reserva
import pandas as pd


#Lee la base de datos CSV de usuarios y crea los objetos usuarios, los agrega al diccionario de Hotel y le agrega las reservas existente a los respectivos clientes, asi como tareas a empleados
def leer_Usuarios(path, Hotel):
    usuarios = pd.read_csv(path)
    
    for _, row in usuarios.iterrows():
        if (row["Rol"] == "Cliente"):
            nuevo_usuario = Cliente(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"])
            Hotel.usuarios[nuevo_usuario.mail] = nuevo_usuario
            for reserva in Hotel.reservas:
                if (reserva.mail == nuevo_usuario.mail):
                    nuevo_usuario.reservas.append(reserva)
        elif (row["Rol"] in ["Mantenimiento", "Administrativo", "Limpieza"]):
            nuevo_empleado = Empleado(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"], int(row["Legajo"]), row["Rol"],row["Estado"])
            Hotel.usuarios[nuevo_empleado.mail] = nuevo_empleado
            tasks = row['Tareas'].split(', ')
            for task in tasks:
                nuevo_empleado.tareas.put(task)
        elif (row["Rol"] == "Administrador"):
            administrador = Administrador(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"], int(row['Legajo']))
            Hotel.usuarios[administrador.mail] = administrador
    
    
#Lee la base de datos CSV de habitaciones y las agrega al hotel
def leer_Habitaciones(path, Hotel):
    habitaciones = pd.read_csv(path)
    
    for _, row in habitaciones.iterrows():
        nueva_habitacion = Habitacion(int(row["Numero"]), int(row["Precio por noche"]), int(row["Capacidad"]), row["Tipo"], row["Banio privado"], row["Balcon"])
        Hotel.habitaciones[nueva_habitacion.numero] = nueva_habitacion

#Lee la base de datos CSV de reservas y las agrega al hotel
def leer_Reservas(path, Hotel):
    reservas = pd.read_csv(path)

    for _, row in reservas.iterrows():
        nueva_reserva = Reserva(row["mail"], row["numero_hab"], row["Fecha_inicio"], row["Fecha_fin"], row['Fecha_reserva'])
        Hotel.reservas.append(nueva_reserva)
        