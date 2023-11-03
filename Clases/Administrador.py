from Usuario import Usuario
from Empleado import Empleado
from queue import Queue

class Administrador(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)

   
    def asignar_tareas(self, empleado: Empleado, tareas: Queue):
            empleado.asignar_tareas(tareas)
            print(f"Tareas asignadas a {empleado.nombre} {empleado.apellido}: {tareas}")


    def dar_empleado_de_alta(self, empleado):
        self.empleados.append(empleado)
        empleado.actualizar_estado("Activo")  # Cambiar el estado del empleado a "Activo"
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de alta como empleado.")


    def dar_empleado_de_baja(self, empleado):
        empleado.actualizar_estado("Inactivo")  # Cambiar el estado del empleado a "Inactivo"
        self.empleados.remove(empleado)
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de baja como empleado.")