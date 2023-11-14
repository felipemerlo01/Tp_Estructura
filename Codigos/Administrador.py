# from Clases.madres.Usuario import Usuario
# from Funciones_extra import validar_num

from Usuario import Usuario
from Funciones_extra import validar_num


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
        for mail, usuario in hotel.usuarios.items():
            if hasattr(usuario,"rol"): # Solo entra si tiene el atributo rol, asi que no afecta a los clientes
                if usuario.rol in categorias:
                    categorias[usuario.rol].append(usuario)
                else:
                    categorias[usuario.rol] = [usuario]
        #Printeamos la información
        for rol, usuarios in categorias.items():
            print(f"\nInventario del personal con rol {rol}:")
            for usuario in usuarios:
                print(f"Nombre: {usuario.nombre} {usuario.apellido}, Mail: {usuario.mail}, Estado: {usuario.estado}")

    # METODO PARA CONTROLAR INGRESOS Y EGRESOS
    def controlar_ingresos_y_egresos(self, hotel):
        empleados_presentes = hotel.generar_ingreso_y_egreso_aleatorio()
        for usuario in empleados_presentes:
            print(f'{usuario.nombre} {usuario.apellido}, Ingreso: {usuario.ingreso}, Egreso: {usuario.egreso}')