from Usuario import Usuario
from Funciones_extra import validar_num, imprimir_tabla

class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str, legajo: int):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.legajo = legajo           

    def dar_empleado_de_alta(self, hotel):
        empleado = hotel.crear_usuario('2')
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de alta como empleado.")
        
    def dar_empleado_de_baja(self, hotel):
        legajo = int(validar_num(input("Legajo del empleado: ")))
        while (legajo == 1):
            print('No puede dar de baja al administrador')
            legajo = int(validar_num(input('Legajo del empleado: ')))
        empleado = hotel.buscar_empleado(legajo)
            
        if (empleado != None):
            empleado.estado = "Inactivo" # Cambiar el estado del empleado a "Inactivo"
            print(f"{empleado.nombre} {empleado.apellido} ha sido dado de baja como empleado.")
        else:
            print(f'El usuario asociado al legajo {legajo} no existe en el sistema.')

    def asignar_empleado_menos_ocupado(self, usuarios, rol):
        lista_empleados_de_interes = []
        for usuario in usuarios.values():
            if (hasattr(usuario, 'rol') and usuario.rol == rol and usuario.estado != "Inactivo"):
                lista_empleados_de_interes.append(usuario)
                
        trabajador_menos_ocupado = min(lista_empleados_de_interes, key=lambda trabajador: trabajador.tareas.qsize())
        return trabajador_menos_ocupado
    
    def asignar_tareas(self, hotel):
        legajo = int(validar_num(input("Legajo del empleado: ")))
        empleado = hotel.buscar_empleado(legajo)
        
        if empleado.estado!="Inactivo":
            tarea = input('Ingrese la tarea a asignar: ')
            
            if (empleado != None):
                empleado.tareas.put(tarea)
                print (f"La tarea fue asignada al empleado/a {empleado.nombre} {empleado.apellido} correctamente")
            else:
                print(f'El usuario asociado al legajo {legajo} no existe en el sistema.')
        else:
            print(f'El usuario asociado al legajo {legajo} está inactivo.')
            
    # METODO DE INVENTARIO DEL PERSONAL
    def ver_inventario_personal(self, hotel):
        categorias = {}
        #Primero agrupamos por rol
        for usuario in hotel.usuarios.values():
            if (hasattr(usuario,"rol") and usuario.estado == 'Activo'): # Solo entra si tiene el atributo rol y esta activo
                if usuario.rol in categorias:
                    categorias[usuario.rol].append(usuario)
                else:
                    categorias[usuario.rol] = [usuario]
        
        columnas = ['Nombre', 'Apellido', 'Mail']
        
        for rol, usuarios in categorias.items():
            print(f"Inventario del personal con rol {rol}:\n")
            informacion = []
            for usuario in usuarios:
                lista_usuario = [usuario.nombre, usuario.apellido, usuario.mail]
                informacion.append(lista_usuario)
            imprimir_tabla(informacion, columnas)
            
    # METODO PARA CONTROLAR INGRESOS Y EGRESOS
    def controlar_ingresos_y_egresos(self, hotel):
        empleados_presentes = hotel.generar_ingreso_y_egreso_aleatorio()
        informacion = []
        for usuario in empleados_presentes:
            lista_usuario = [usuario.nombre, usuario.apellido, usuario.ingreso, usuario.egreso]
            informacion.append(lista_usuario)
        
        columnas = ['Nombre', 'Apellido', 'Ingreso', 'Egreso']
        print('Los ingresos y egresos de los empleados de hoy son:\n')
        imprimir_tabla(informacion, columnas)