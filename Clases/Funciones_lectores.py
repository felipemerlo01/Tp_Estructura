# Funciones de lectura de las bases de datos: 
from Cliente import Cliente
from Empleado import Empleado
from Administrador import Administrador
from Habitacion import Habitacion
from Reserva import Reserva
import pandas as pd
from datetime import datetime


#Lee la base de datos CSV de usuarios y crea los objetos usuarios, los agrega al diccionario de Hotel y le agrega las reservas existente a los respectivos clientes, asi como tareas a empleados
def leer_Usuarios(path, Hotel):
    usuarios = pd.read_csv(path)
    
    for _, row in usuarios.iterrows():
        if (row["Rol"] == "Cliente"):
            nuevo_usuario = Cliente(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"])
            Hotel.usuarios[nuevo_usuario.mail] = nuevo_usuario
            for reserva in Hotel.reservas:
                if (reserva.mail_usuario == nuevo_usuario.mail):
                    nuevo_usuario.reservas.append(reserva)
        elif (row["Rol"] in ("Mantenimiento", "Administrativo", "Limpieza")):
            nuevo_empleado = Empleado(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"], int(row["Legajo"]), row["Rol"], row["Estado"])
            Hotel.usuarios[nuevo_empleado.mail] = nuevo_empleado
            #tasks = row['Tareas'].split(', ')
            tasks=""    #FIJARSE PORQ LO LEE COMO FLOAT
            for task in tasks:
                nuevo_empleado.tareas.put(task)
        elif (row["Rol"] == "admin"):
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
        nueva_reserva = Reserva(row["Mail"], int(row["Numero de habitacion"]), row["Check-in"], row["Check-out"], row['Fecha reserva'], int(row['Gastos buffet']), int(row['Gastos minibar']))
        nueva_reserva.habitacion=Hotel.habitaciones[nueva_reserva.num_hab]
        nueva_reserva.gastos_ocupacion = (datetime.strptime(nueva_reserva.check_out, "%d/%m/%Y")-datetime.strptime(nueva_reserva.check_in, "%d/%m/%Y")).days * nueva_reserva.habitacion.precio
        Hotel.reservas.append(nueva_reserva)
        