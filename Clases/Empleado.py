from datetime import datetime, timedelta
from queue import Queue
from Usuario import Usuario
from random import randint
from Funciones_extra import verificar_mail

class Empleado(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str, legajo: int, rol: str, estado = 'Activo'):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.rol = rol
        self.estado = estado
        self.registro_ingresos = []  # Lista para registrar los ingresos del empleado
        self.registro_egresos = []  # Lista para registrar los egresos del empleado
        self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas
        # self.presente= None

    def disponibilidad_habitacion(self, diccionario_habitaciones, lista_reservas, check_in, check_out, criterios):
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
    
    def agregar_tarea_automatica(self, num_habitacion, buffet=False):
        if (self.rol == 'Mantenimiento'):
            self.tareas.put(f'Reponer minibar en {num_habitacion}')
        elif (self.rol == 'Limpieza'):
            if (buffet):
                self.tareas.put(f'Limpieza en el buffet de {num_habitacion}')
            else:
                self.tareas.put(f'Preparacion de la habitacion en {num_habitacion}')

    # Realizar tarea siguiente
    def realizar_siguiente_tarea(self):
        if (not self.tareas.empty()):
            tarea = self.tareas.get()
            print(f"{self.nombre} {self.apellido} realizando tarea: {tarea}")
        else:
            print("Usted no tiene tareas pendientes para realizar.")

    # Visualizar tareas pendientes del empleado
    def visualizar_tareas_pendientes(self):
        if (not self.tareas.empty()):
            tupla_tareas = tuple(self.tareas)
            num = 1
            for tarea in tupla_tareas:
                print(f'{num}. {tarea}')
                num += 1
        else:
            print("Enhorabuena! Usted no tiene tareas pendientes.")
    
    # Buscar todas las reservas hechas por un cliente, al cual buscas por su mail
    def historial_de_reservas(self):
        mail_cliente = verificar_mail(input("Ingrese el mail del cliente: "))
        if mail_cliente in self.usuarios:
            if len(self.usuarios[mail_cliente].reservas) > 0:
                print("Se listan las siguientes Reservas: ")
                for reserva in self.usuarios[mail_cliente].reservas:
                    print(f'Fecha reserva: {reserva.fecha_reserva}\n Número de Habitación: {reserva.habitacion.numero}  \n Check-in: {reserva.check_in}\n Check-out: {reserva.check_out}\n Gastos Total: {reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos_ocupacion}  \n\n')
            else:
                print("El cliente seleccionado no tiene reservas registradas")
        else:
            print('No existe el cliente en el sistema.')

    # METODO NOMINA DE CLIENTES DEL HOTEL (clientes actualmente hospedados en el hotel)
    # 1. recorrer lista de reservas del hotel --> buscar las reservas activas al dia de hoy
    # 2. agarrar los mails de usuario de esas reservas, guardar en una lista
    # 3. iterar por hotel.usuarios y agarrar a los usuarios que tengan algguno de estos mails
    # 4. imprimir la informacion de cada uno de esos usuarios (nombre, apellido, mail)
    def nomina_de_clientes(self,hotel):
        for reserva in hotel.reservas:
            if reserva.habitacion.ocupada == True:
                pass

    # El empleado hace el ingreso manualmente
    def registro_ingreso(self):
        #se hace el ingreso de forma automática entre las 8-9 am 
        hora_ingresada = (datetime.strptime("08:00", "%H:%M") + timedelta(minutes=randint(0,59))).strftime("%H:%M")
        hoy = datetime.date.today().strftime('%d/%m/%Y')
       
        ingreso = (hoy, hora_ingresada)
        self.registro_ingresos.append(ingreso)

    # El empleado hace el egreso manualmente
    def registro_egreso(self):
        hora_egreso = (datetime.strptime("20:00", "%H:%M") + timedelta(minutes=randint(0,59))).strftime("%H:%M")
        hoy = datetime.date.today().strftime('%d/%m/%Y')
        
        egreso = (hoy, hora_egreso)
        self.registro_egresos.append(egreso)


# #estos metodos puede llegar a quedar pero en realidad se hacen automáticamnte     

#     def realizar_check_in(self, habitacion):
#         # Implementar lógica para realizar el check-in
#         # Actualizar el estado de la habitación a "Ocupada"
#         # se tiene que hacer automaticamente 
#         if habitacion.ocupada == True:
#             fecha_actual = datetime.now()
#             habitacion.ocupada = False
#             habitacion.fecha_check_in = fecha_actual
#             self.registro_ingreso()
#             print(f"Check-in realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")

#     def realizar_check_out(self, habitacion):
#         # Implementar lógica para realizar el check-out
#         # Actualizar el estado de la habitación a "Disponible"
#         #se tiene que hacer automaticamente 
#         if habitacion.estado == "Ocupada":
#             fecha_actual = datetime.now()
#             habitacion.estado = "Disponible"
#             habitacion.fecha_check_out = fecha_actual
#             self.registro_egreso()
#             print(f"Check-out realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")