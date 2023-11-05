import csv 
import pandas as pd
from Clases.Hotel import Hotel

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
4. Ver gastos  
5. Volver''')

def menu_Administrador(): 
    print('''
1. Dar empleado de alta
2. Dar empleado de baja
3. Asignar tareas
4. Control de ingreso y egreso
5. Inventario del Personal: Administrativo, Mantenimiento y Limpieza
6. Recaudación diaria
7. Volver''')
    
def menu_Personal_Administrativo():
    print('''
1. Historial de sus reservas
2. Nomina de clientes del hotel
3. Informes estadísticos
4. Volver''')
    
def menu_Informe_estadístico(): 
    print('''
1. Porcentaje de ocupación del hotel
2. Porcentaje de ocupacion de acuerdo al tipo de habitación
3. Cantidad de clientes por tipo
4. Volver''')
    
def menu_Mant_Limp(): 
    print('''
1. Registro ingreso
2. Registro egreso
3. Visualización de las tareas activas
4. Volver''')
    
    # NO ENTIENDO SI LOS DE MANTENIMIENTO Y LIMPIEZA TIENEN ACCESO AL MENÚ O NO?
    # SI NO  TIENEN ACCESO AL MENU PERO SI SON USUARIOS ENTONCES DE QUE SIRVE QUE TENGAN CONTRASEÑA?
    # SI TIENEN ACCESO AL MENU, LA UNICA OPCION QUE LES APARECE EN EL MENU ES HACER SUS TAREAS O SALIR?

#faltan todos los cosos 
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
                menu_Cliente()
                opcion_admin= validar_opcion_menu(input("Ingrese una opción: "),7)
                if opcion_admin == '1':
                    pass
                elif opcion_admin == '2': 
                    pass
                elif opcion_admin == '3':
                    pass
                elif opcion_admin == '4':
                    pass
                elif opcion_admin == '5':
                    pass
                elif opcion_admin == '6':
                    pass
                elif opcion_admin == '7':
                    pass
                else: 
                    coninuar=False
            else:
                menu_Personal_Administrativo()
                opcion_personal_admin= validar_opcion_menu(input("Ingrese una opción: "),3)
                if  opcion_personal_admin== '1':
                    pass
                elif opcion_personal_admin== '2':
                    pass
                else:
                    continuar = False
        
                # mostrar menu para personal administrativo (y mant y limpieza ?¿)
        else:
            menu_Cliente()
            opcion_cliente = validar_opcion_menu(input('Ingrese una opción: '), 6)
            if opcion_cliente == '1':
                pass
            elif opcion_cliente == '2':
                pass

            elif (opcion_cliente == '3'):
                pass
            elif (opcion_cliente == '4'):
                pass
            elif (opcion_cliente == '5'):
                pass
            
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
