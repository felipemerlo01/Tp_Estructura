from Clases.Hotel import Hotel
from Clases.Funciones_extra import leer_Usuarios, leer_Habitaciones, leer_Reservas, menu_principal, menu_registro, validar_opcion_menu, menu_Cliente, menu_Administrador, menu_Personal_Administrativo, menu_Informe_estadístico, menu_Mant_Limp
    
    # NO ENTIENDO SI LOS DE MANTENIMIENTO Y LIMPIEZA TIENEN ACCESO AL MENÚ O NO?
    # SI NO  TIENEN ACCESO AL MENU PERO SI SON USUARIOS ENTONCES DE QUE SIRVE QUE TENGAN CONTRASEÑA?
    # SI TIENEN ACCESO AL MENU, LA UNICA OPCION QUE LES APARECE EN EL MENU ES HACER SUS TAREAS O SALIR?

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
