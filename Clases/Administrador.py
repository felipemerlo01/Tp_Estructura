from Usuario import Usuario
from queue import Queue

class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str, legajo: int):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
    
    def asignar_tareas(self, empleado, tareas: Queue):
        empleado.asignar_tareas(tareas)
        print (f"La tarea de {empleado.rol.lower()} fue asiganda a {empleado.nombre} {empleado.apellido}") #se le puede poner el nombre así asignadas a {empleado.nombre} {empleado.apellido}                  

    def dar_empleado_de_alta(self, hotel):
        empleado = hotel.crear_usuario('2')
        hotel.usuarios[empleado.mail] = empleado
        empleado.estado = 'Activo'  # Cambiar el estado del empleado a "Activo"
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de alta como empleado.")
    
    def dar_empleado_de_baja(self, hotel):
        nombre = input("Nombre del empleado: ").capitalize()
        apellido = input("Apellido del empleado: ").capitalize()
        
        empleado = hotel.buscar_empleado(nombre, apellido)
            
        if (empleado != None):
            empleado.estado = "Inactivo" # Cambiar el estado del empleado a "Inactivo"
            self.empleados.remove(empleado)
            print(f"{empleado.nombre} {empleado.apellido} ha sido dado de baja como empleado.")
        else:
            print(f'{nombre} {apellido} no es un usuario en el sistema.')
        
    def asignar_empleado_menos_ocupado(self, usuarios, rol):
        lista_empleados_de_interes = []
        for usuario in usuarios.values():
            if (hasattr(usuario, 'rol') and usuario.rol == rol):
                lista_empleados_de_interes.append(usuario)
                
        trabajador_menos_ocupado = min(lista_empleados_de_interes, key=lambda trabajador: trabajador.tareas.qsize())
        return trabajador_menos_ocupado
        
    