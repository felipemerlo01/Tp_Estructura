import csv 
import pandas as pd
from Hotel import Hotel

Clientes=[]
Habitaciones=[]
Reservas=[]

lector_usuario = open("usuarios.csv","r")
usuarios = pd.read_csv('usuarios.csv')


lector_habitacion = open("habitaciones.csv","r")
habitaciones = pd.read_csv('habitaciones.csv')


lector_reservas = open("reservas.csv","r")
reservas = pd.read_csv('reservas.csv')

def menu_principal():
    print('''Bienvenido al menu:
1. Iniciar sesión
2. Registrar usuario
3. Salir''')
    
def menu_registro():
    print('''
1. Registrarse como cliente
2. Registrarse como empleado
3. Volver''')
    
def validar_opcion_menu(opcion, cantidad_opciones):
    while (opcion not in range(1, cantidad_opciones+1)):
        opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
    return opcion

def menu_Cliente():
    print('''
1. Hacer reserva
2. Ir al buffet
3. Usar el minibar
4. Volver''')

def menu_Administrador(): # REVISAR LO QUE PUEDE HACER EL ADMINSITRADOR !
    print('''
1. Dar empleado de alta
2. Dar empleado de baja
3. Asignar tareas
4. Volver''')
    
def menu_Empleado(): # REVISAR LO QUE PUEDE HACER EL PERSONAL ADMINISTRATIVO.
    print('''
1. Hacer reserva
2. Ir al buffet
3. Usar el minibar
4. Volver''')
    
    # NO ENTIENDO SI LOS DE MANTENIMIENTO Y LIMPIEZA TIENEN ACCESO AL MENÚ O NO?
    # SI NO  TIENEN ACCESO AL MENU PERO SI SON USUARIOS ENTONCES DE QUE SIRVE QUE TENGAN CONTRASEÑA?
    # SI TIENEN ACCESO AL MENU, LA UNICA OPCION QUE LES APARECE EN EL MENU ES HACER SUS TAREAS O SALIR?

# El menu en si mismo
continuar = True
cargado = False
while (continuar == True):
    
    if (not cargado):
        POO = Hotel('Patagonia: Oasis y Ocio')
        # FALTA! leer bases de datos csv y cargarlas al objeto POO
        cargado = True
    
    menu_principal()
    opcion = validar_opcion_menu(input('Ingrese una opción: '), 3)
    if (opcion == '1'):
        usuario = POO.iniciar_sesion()
        if (hasattr(usuario, 'legajo')):
            if (usuario.legajo == 1):
                # mostrar menu administrador
            else:
                # mostrar menu para personal administrativo (y mant y limpieza ?¿)
        else:
            menu_Cliente()
            opcion_Cliente = validar_opcion_menu(input('Ingrese una opción: '), 4)
            if (opcion_Cliente == '1'):
            elif (opcion_Cliente == '2'):
            elif (opcion_Cliente == '3'):
            
    elif (opcion == '2'):
        menu_registro()
        registro_opcion = validar_opcion_menu(input("Ingrese una opción de registro: "), 3)
        if (registro_opcion == '1'):
            POO.crear_usuario('1')
            usuario = POO.usuarios[-1]
        elif (registro_opcion == '2'):
            POO.crear_usuario('2')
            usuario = POO.usuarios[-1]
    
    else:
        continuar = False
