import csv 
import pandas as pd

Clientes=[]
Habitaciones=[]
Reservas=[]

lector_usuario = open("usuarios.csv","r")
usuarios = pd.read_csv('usuarios.csv')


lector_habitacion = open("habitaciones.csv","r")
habitaciones = pd.read_csv('habitaciones.csv')


lector_reservas = open("reservas.csv","r")
reservas = pd.read_csv('reservas.csv')
print

def menu():
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")

def menu_registro():
    print("1. Registrarse como cliente")
    print("2. Registrarse como empleado")

continuar = True
while continuar:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        pass
    elif opcion == "2":
        menu_registro()
        registro_opcion = input("Ingrese una opción de registro: ")
        if registro_opcion == "1":
            pass #metodo registrar cliente
        elif registro_opcion == "2":
            pass #metodo registrar empleado
        else:
            print("Opción de registro no válida.")
    elif opcion == "3":
        continuar = False
    else:
        print("Opción no válida")
