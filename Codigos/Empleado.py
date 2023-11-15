from datetime import datetime, timedelta
from queue import Queue
from Usuario import Usuario
from random import randint
from Funciones_extra import verificar_mail, imprimir_tabla

class Empleado(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str, legajo: int, rol: str, estado = 'Activo'):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.rol = rol
        self.estado = estado
        self.ingreso = None
        self.egreso = None
        self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas

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
            tupla_tareas = tuple(self.tareas.queue)
            num = 1
            for tarea in tupla_tareas:
                print(f'{num}. {tarea}')
                num += 1
        else:
            print("Enhorabuena! Usted no tiene tareas pendientes.")
    
    # Buscar todas las reservas hechas por un cliente, al cual buscas por su mail
    def historial_de_reservas(self, hotel):
        mail_cliente = verificar_mail(input("Ingrese el mail del cliente: "))
        if mail_cliente in hotel.usuarios:
            if len(hotel.usuarios[mail_cliente].reservas) > 0:
                informacion = []
                for reserva in hotel.usuarios[mail_cliente].reservas:
                    gasto_total = reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos_ocupacion
                    lista_reserva = [reserva.fecha_reserva, reserva.habitacion.numero, reserva.check_in, reserva.check_out, gasto_total]
                    informacion.append(lista_reserva)

                columnas = ['Fecha reserva', 'Habitación', 'Check-in', 'Check-out', 'Gastos total']
                
                print(f"Se listan las siguientes reservas de {hotel.usuarios[mail_cliente].nombre} {hotel.usuarios[mail_cliente].apellido}:\n")
                imprimir_tabla(informacion, columnas)
            else:
                print("El cliente seleccionado no tiene reservas registradas")
        else:
            print('No existe el cliente en el sistema.')

    def nomina_de_clientes(self, hotel):
        hoy = datetime.now()
        mails_clientes_actuales = []
        for reserva in hotel.reservas:
            check_in_dt = datetime.strptime(reserva.check_in + ' 15:00', "%d/%m/%Y %H:%M")
            check_out_dt = datetime.strptime(reserva.check_out + ' 11:00', "%d/%m/%Y %H:%M")
            if (check_in_dt < hoy < check_out_dt): 
                mails_clientes_actuales.append(reserva.mail_usuario)
        if (len(mails_clientes_actuales) > 0):
            informacion = []
            for mail in hotel.usuarios:
                if (mail in mails_clientes_actuales):
                    usuario = hotel.usuarios[mail]
                    lista_usuario = [usuario.nombre, usuario.apellido, usuario.mail]
                    informacion.append(lista_usuario)
            
            columnas = ['Nombre', 'Apellido', 'Mail']
            
            print('Se listan los siguientes clientes hospedados actualmente: \n')
            imprimir_tabla(informacion, columnas)
        else:
            print('No hay clientes hospedados actualmente en el hotel.')

    # El empleado hace el ingreso manualmente
    def registro_ingreso(self):
        #se hace el ingreso de forma automática entre las 8-9 am 
        hora_ingresada = (datetime.strptime("08:00", "%H:%M") + timedelta(minutes=randint(0,59))).strftime("%H:%M")
        self.ingreso =  hora_ingresada

    # El empleado hace el egreso manualmente
    def registro_egreso(self):
        hora_egreso = (datetime.strptime("20:00", "%H:%M") + timedelta(minutes=randint(0,59))).strftime("%H:%M")
        self.egreso =  hora_egreso
