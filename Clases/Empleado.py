from datetime import datetime, timedelta
from queue import Queue
from Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str, legajo: int, rol: str, estado = 'Activo'):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.rol = rol
        self.estado = estado
        self.registro_ingresos = []  # Lista para registrar los ingresos del empleado
        self.registro_egresos = []  # Lista para registrar los egresos del empleado
        self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas

    def disponibilidad_habitacion(diccionario_habitaciones, lista_reservas, check_in, check_out, criterios):
        # creo un diccionario con sets de las fechas en las que esta ocupada la habitacion
        disponibilidad_habitaciones = {}
        for key in diccionario_habitaciones:
            disponibilidad_habitaciones[key] = set()
        
        # segun las reservas existentes agrego cada dia en el rango de check-in check-out (cuando va a estar ocupada)
        for reserva in lista_reservas:
            id_habitacion = reserva.habitacion.numero
            check_in_habitacion = datetime.strptime(reserva.check_in, "%d/%m/%Y")
            check_out_habitacion = datetime.strptime(reserva.check_out, "%d/%m/%Y")
            
            fecha_actual = check_in_habitacion + timedelta(days=1)
            while (fecha_actual < check_out_habitacion):
                disponibilidad_habitaciones[id_habitacion].add(fecha_actual)
                fecha_actual += timedelta(days=1)
        
        # veo segun los datos de mi nueva reserva si hay una habitacion disponible
        for key in diccionario_habitaciones:
            if (disponibilidad_habitaciones[key].isdisjoint({check_in, check_out})):
                cumple_criterios = True
                if ("Precio" in criterios and diccionario_habitaciones[key].precio > criterios['Precio']):
                    cumple_criterios = False
                if ("Capacidad" in criterios and diccionario_habitaciones[key].capacidad < criterios['Capacidad']):
                    cumple_criterios = False
                if ("Banio" in criterios and diccionario_habitaciones[key].banio_privado != criterios['Banio']):
                    cumple_criterios = False  
                if ("Balcon" in criterios and diccionario_habitaciones[key].balcon != criterios['Balcon']):
                    cumple_criterios = False    
                if cumple_criterios:
                    return diccionario_habitaciones[key] # si encuentra la habitacion termina de iterar y el metodo finaliza
        
        # si itera todas las habitaciones y ninguna cumple con las condiciones, termina el metodo, retorna None
        return

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