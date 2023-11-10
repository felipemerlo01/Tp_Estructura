from Clases.Hotel import Hotel
from Clases.Funciones_extra import menu_principal, menu_registro, validar_opcion_menu, menu_Cliente, menu_Administrador, menu_Personal_Administrativo, menu_Informe_estadístico, menu_Mant_Limp
from Clases.Funciones_lectores import leer_Usuarios, leer_Habitaciones, leer_Reservas

# El menu en si mismo
continuar = True
cargado = False
path = 'Tp_Estructura-1/Bases de datos/'

while (continuar):
    if (not cargado):
        POO = Hotel('Patagonia: Oasis y Ocio')
        leer_Habitaciones(path+'db_Habitaciones.csv', POO)
        leer_Reservas(path+'db_Reservas.csv', POO)
        leer_Usuarios(path+'db_Usuarios.csv', POO)
        cargado = True
    
    menu_principal()
    opcion = validar_opcion_menu(input('Ingrese una opción: '), 3)
    if (opcion == '1'):
        usuario = POO.iniciar_sesion()
        print(f'Se inició sesión correctamente. Bienvenido.')
        
        if (hasattr(usuario, 'legajo')):
            if (usuario.legajo == 1): # Menu para el Administrador
                volver = False
                while (not volver):
                    menu_Administrador()
                    opcion_admin = validar_opcion_menu(input(" Ingrese una opción: "), 7)
                    if opcion_admin == '1': # Dar empleado de alta
                        usuario.dar_empleado_de_alta(POO) 
                    elif opcion_admin == '2': # Dar empleado de baja
                        usuario.dar_empleado_de_baja(POO)          
                    elif opcion_admin == '3': # Asignar tarea a un empleado
                        usuario.asignar_tareas(POO)
                    elif opcion_admin == '4': # Control de ingreso y egreso
                        pass
                    elif opcion_admin == '5': # Ver inventario del personal
                        pass
                    elif opcion_admin == '6': # Recaudacion diaria
                        pass
                    else:
                        volver = True
            else:
                if (usuario.rol == 'Administrativo'): # Menu para empleados administrativos
                    volver_1 = False
                    while (not volver):
                        menu_Personal_Administrativo()
                        opcion_personal_admin = validar_opcion_menu(input("Ingrese una opción: "), 4)
                        if (opcion_personal_admin == '1'): # Historial de reservas
                            pass
                        elif (opcion_personal_admin == '2'): # Nomina de clientes del hotel
                            pass
                        elif (opcion_personal_admin == '3'): # Informes estadisticos (sub-menu)
                            volver_2 = False
                            while (not volver_2):
                                menu_Informe_estadístico()
                                opcion_informe = validar_opcion_menu(input("Ingrese una opción: "), 4)
                                if (opcion_informe == '1'): # Porcentaje de ocupacion del hotel
                                    pass
                                elif (opcion_informe == '2'): # Porcentaje de ocupacion de acuerdo al tipo de habitacion
                                    pass
                                elif (opcion_informe == '3'): # Cantidad de clientes por tipo
                                    pass
                                else:
                                    volver_2 = True
                        else:
                            volver_1 = True
                
                else: # Menu para empleados de limpieza y mantenimiento
                    volver = False
                    while (not volver):
                        menu_Mant_Limp()
                        opcion_mant_limp = validar_opcion_menu(input("Ingrese una opción: "), 3)
                        if (opcion_mant_limp == '1'): # Visualización de las tareas pendientes
                            usuario.visualizar_tareas_pendientes()
                        elif (opcion_mant_limp == '2'): # Realizar tarea pendiente
                            usuario.realizar_siguiente_tarea()
                        else:
                            volver = True
        else: # Menu para clientes
            volver = False
            while (not volver):
                menu_Cliente()
                opcion_cliente = validar_opcion_menu(input('Ingrese una opción: '), 5)
                if (opcion_cliente == '1'): # Cliente hace una reserva
                    usuario.hacer_reserva(POO)
                elif (opcion_cliente == '2'): # Cliente va al buffet
                    usuario.ir_al_buffet(POO) 
                elif (opcion_cliente == '3'): # Cliente va el minibar
                    usuario.usar_el_minibar(POO) 
                elif (opcion_cliente == '4'): # Cliente ve sus reservas activas
                    usuario.ver_reservas_activas()
                else:
                    volver = True
    
    elif (opcion == '2'): # Menu para registrarse
        menu_registro()
        registro_opcion = validar_opcion_menu(input("Ingrese una opción de registro: "), 3)
        if (registro_opcion == '1'): # Registrarse como cliente
            usuario = POO.crear_usuario(registro_opcion)
        elif (registro_opcion == '2'): # Registrarse como empleado
            usuario = POO.crear_usuario(registro_opcion)
    else:
        POO.actualizar_bases_de_datos(path)
        continuar = False
