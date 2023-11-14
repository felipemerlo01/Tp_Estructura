from Hotel import Hotel
from Funciones_extra import menu_principal, menu_registro, validar_opcion_menu, menu_Cliente, menu_Administrador, menu_Personal_Administrativo, menu_Mant_Limp
from Funciones_lectura_path import leer_Usuarios, leer_Habitaciones, leer_Reservas, obtener_path
from datetime import datetime

path = obtener_path()

if (path is not None):
    continuar = True
    cargado = False
    # El menu en si mismo
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
            print(f'Se inició sesión correctamente. Bienvenido/a {usuario.nombre}.')
            
            if (hasattr(usuario, 'legajo')):
                if (usuario.legajo == 1): # Menu para el Administrador
                    volver = False
                    while (not volver):
                        menu_Administrador()
                        opcion_admin = validar_opcion_menu(input("Ingrese una opción: "), 7)
                        if opcion_admin == '1': # Dar empleado de alta
                            usuario.dar_empleado_de_alta(POO) 
                        elif opcion_admin == '2': # Dar empleado de baja, NO se puede activar nuevamente
                            usuario.dar_empleado_de_baja(POO)          
                        elif opcion_admin == '3': # Asignar tarea a un empleado
                            usuario.asignar_tareas(POO)
                        elif opcion_admin == '4': # Control de ingreso y egreso
                            usuario.controlar_ingresos_y_egresos(POO)
                        elif opcion_admin == '5': # Ver inventario del personal
                            usuario.ver_inventario_personal(POO)
                        elif opcion_admin == '6': # Recaudacion diaria
                            fecha_actual = datetime.now().strftime("%d/%m/%Y")
                            hora_actual = datetime.now().strftime("%H:%M")
                            print(f"La recaudación diaria de hoy {fecha_actual} a las {hora_actual} es de ${POO.recaudacion_diaria()}")
                        else: 
                            volver = True
                else:
                    if (usuario.rol == 'Administrativo'): # Menu para empRleados administrativos
                        volver_1 = False
                        while (not volver_1):
                            menu_Personal_Administrativo()
                            opcion_personal_admin = validar_opcion_menu(input("Ingrese una opción: "), 6)
                            if (opcion_personal_admin == '1'): # Historial de reservas
                                usuario.historial_de_reservas(POO)

                            elif (opcion_personal_admin == '2'): # Nomina de clientes del hotel
                                usuario.nomina_de_clientes(POO)

                            elif (opcion_personal_admin == '3'): # Informe estadístico
                                POO.crear_informe_estadistico()

                            elif (opcion_personal_admin == '4'): # Visualizar tareas pendientes
                                usuario.visualizar_tareas_pendientes()     
                            
                            elif (opcion_personal_admin == '5'): # Realizar tarea pendiente
                                usuario.realizar_siguiente_tarea()         
                            
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
