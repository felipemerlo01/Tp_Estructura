from Clases.Hotel import Hotel
from Clases.Funciones_extra import menu_principal, menu_registro, validar_opcion_menu, menu_Cliente, menu_Administrador, menu_Personal_Administrativo, menu_Informe_estadístico, menu_Mant_Limp
from Clases.Funciones_lectores import leer_Usuarios, leer_Habitaciones, leer_Reservas

# El menu en si mismo
continuar = True
cargado = False
path = 'Tp_Estructura-1/Bases de datos/'

while (continuar == True):
    if (not cargado):
        POO = Hotel('Patagonia: Oasis y Ocio')
        leer_Habitaciones(path+'db_Habitaciones.csv', POO)
        leer_Reservas(path+'db_Reservas.csv', POO)
        leer_Usuarios(path+'db_Usuarios.csv', POO)
        cargado = True
    
    POO.actualizar_datos_totales()
    
    menu_principal()
    opcion = validar_opcion_menu(input('Ingrese una opción: '), 3)
    if (opcion == '1'):
        usuario = POO.iniciar_sesion()
        print(f'Se inició sesión correctamente. Bienvenido.')
        if (hasattr(usuario, 'legajo')):
            if (usuario.legajo == 1):
                menu_Administrador()
                opcion_admin = validar_opcion_menu(input(" Ingrese una opción: "), 7)
                if opcion_admin == '1': # Dar empleado de alta
                    usuario.dar_empleado_de_alta() 
                elif opcion_admin == '2': # Dar empleado de baja
                    usuario.dar_empleado_de_baja()          
                elif opcion_admin == '3':
                    pass
                elif opcion_admin == '4':
                    pass
                elif opcion_admin == '5':
                    pass
                elif opcion_admin == '6':
                    pass
            else:
                if (usuario.rol == 'Administrativo'):
                    menu_Personal_Administrativo()
                    opcion_personal_admin = validar_opcion_menu(input("Ingrese una opción: "), 4)
                    if (opcion_personal_admin == '1'):
                        pass
                    elif (opcion_personal_admin == '2'):
                        pass
                else:
                    menu_Mant_Limp()
                    opcion_mant_limp = validar_opcion_menu(input("Ingrese una opción: "), 5)
                    if (opcion_mant_limp == '1'):
                        usuario.registro_ingreso()
                        print ("Registro de ingreso realizado")
                    elif (opcion_mant_limp == '2'):
                        usuario.registro_egreso()
                        print ("Registro de egreso realizado")
                    elif (opcion_mant_limp == '3'):
                        pass
                    elif (opcion_mant_limp == '4'):
                        pass
        else:
            menu_Cliente()
            opcion_cliente = validar_opcion_menu(input('Ingrese una opción: '), 5)
            if (opcion_cliente == '1'):
                pass
            elif (opcion_cliente == '2'):
                pass
            elif (opcion_cliente == '3'):
                pass
            elif (opcion_cliente == '4'):
                pass
    elif (opcion == '2'):
        menu_registro()
        registro_opcion = validar_opcion_menu(input("Ingrese una opción de registro: "), 3)
        if (registro_opcion == '1'):
            usuario = POO.crear_usuario(registro_opcion)
        elif (registro_opcion == '2'):
            usuario = POO.crear_usuario(registro_opcion)
    else:
        continuar = False
