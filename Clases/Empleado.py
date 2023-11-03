from datetime import datetime
from queue import Queue
from Usuario import Usuario

class Empleado(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str, legajo: int, rol: str, estado = 'Activo'):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.rol = rol
        self.estado = estado
        self.registro_ingresos = []  # Lista para registrar los ingresos del empleado
        self.registro_egresos = []  # Lista para registrar los egresos del empleado
        self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas

    def registro_ingreso(self):
        # Registrar la fecha y hora actual de ingreso
        fecha_actual = datetime.now()
        ingreso = {
            'fecha': fecha_actual.strftime('%Y-%m-%d'),
            'hora': fecha_actual.strftime('%H:%M')}
        self.registro_ingresos.append(ingreso)

    def registro_egreso(self):
        # Registrar la fecha y hora actual de egreso
        fecha_actual = datetime.now()
        egreso = {
            'fecha': fecha_actual.strftime('%Y-%m-%d'),
            'hora': fecha_actual.strftime('%H:%M')}
        self.registro_egresos.append(egreso)
    
    def realizar_check_in(self, habitacion):
        # Implementar lógica para realizar el check-in
        # Actualizar el estado de la habitación a "Ocupada"
        if habitacion.estado == "Disponible":
            fecha_actual = datetime.now()
            habitacion.estado = "Ocupada"
            habitacion.fecha_check_in = fecha_actual
            self.registro_ingreso()
            print(f"Check-in realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")

    def realizar_check_out(self, habitacion):
        # Implementar lógica para realizar el check-out
        # Actualizar el estado de la habitación a "Disponible"
        if habitacion.estado == "Ocupada":
            fecha_actual = datetime.now()
            habitacion.estado = "Disponible"
            habitacion.fecha_check_out = fecha_actual
            self.registro_egreso()
            print(f"Check-out realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
    
    #aca va a aparecer el estado que tiene el empleado dependiendo de lo que decide el administrativo 

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    #aca se va a ver la tarea que tiene asiganda ese empleado
    def asignar_tareas(self, tareas):
        for tarea in tareas:
            self.tareas.put(tarea) #el empleado tiene un cola de tareas 

    def realizar_siguiente_tarea(self):
        if not self.tareas.empty():
            tarea = self.tareas.get()
            print(f"{self.nombre} {self.apellido} realizando tarea: {tarea}")

    def finalizar_tarea(self):
        # Implementar lógica de finalizar tarea de limpieza y mantenimiento
            pass