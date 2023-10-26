import csv 

Clientes=[]
Habitaciones=[]
Reservas=[]

lector = open("usuarios.csv","r")

lector = open("habitaciones.csv","r")

lector = open("reservas.csv","r")


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
