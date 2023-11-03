from datetime import datetime
from queue import Queue

class Usuario:
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.dni = dni
        self.mail = mail
        self.contrasena = contrasena


#esta parte del administrador esta ok 





    
    




""" 
Usuario -> Cliente
        -> Administrador  ¿que cosas hace?
        -> Empleado     Metodo (registrar_ingreso), Metodo(registrar_egreso)
                        --> Limpieza        --> Metodo (finaliizar_tarea) 
                        --> Mantenimiento    -> Metodo (finalizar_tarea)  
                        --> Administrativo   --> Metodo (asignar_tareas)

Cliente -> hacer_reserva, ir_al_buffet, usar_el_minibar

Administrativo -> check_in, check_out, hacer_reserva, asignar_tareas, ver_inventario_personal

Administrador -> dar_empleado_de_alta, dar_empleado_de_baja

"""
'''# Ejemplo de uso
admin = Adminitrador("Admin", "Adminson", 35, "M", 123456789, "admin@example.com", "adminpass")
empleado = Empleado("Empleado", "Ejemplo", 25, "F", 987654321, "empleado@example.com", "empleadopass", 1001)

admin.dar_empleado_de_baja(empleado)  # El administrador da de baja al empleado y cambia su estado a "Inactivo"
print(f"Estado del empleado: {empleado.estado}")
En este ejemplo, el administrador puede dar de baja a un empleado y cambiar su estado a "Inactivo". El método dar_empleado_de_baja en Adminitrador llama al método actualizar_estado del empleado para realizar esta tarea. El estado del empleado se refleja y se puede consultar en cualquier momento.

'''





