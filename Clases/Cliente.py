#from ClasesUsuario import Usuario
from Reserva import Reserva
from datetime import datetime, date
from Funciones_extra import validar_fecha, validar_fecha_posteriori, validar_si_no, validar_capacidad_min, validar_precio, validar_opcion, validar_num
from queue import LifoQueue
from Usuario import Usuario
from Empleado import Empleado
import inspect

class Cliente(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.gastado = 0 
        self.reservas = []

    def recolectar_criterios_interes(self):
        criterios_elegidos = {} # Asimismo hay que validarlos
        
        criterio = validar_si_no(input("¿Desea filtrar por capacidad? (Si/No): ").capitalize())
        if (criterio == "Si"):
            capacidad_minima = int(validar_capacidad_min(input("Capacidad mínima deseada: ")))
            criterios_elegidos['Capacidad'] = capacidad_minima

        criterio = validar_si_no(input("¿Desea filtrar por precio por noche? (Si/No): ").capitalize())
        if (criterio == "Si"):
            precio_maximo = int(validar_precio(input("Precio maximo deseado: ")))
            criterios_elegidos['Precio'] = precio_maximo

        criterio = validar_si_no(input("¿Desea filtrar por baño privado? (Si/No): ").capitalize())
        if (criterio == "Si"):
            bano_privado = validar_si_no(input("¿Requiere baño privado? (Si/No): ").capitalize()) == "Si"
            criterios_elegidos['Banio'] = bano_privado

        criterio = validar_si_no(input("¿Desea filtrar por balcón? (Si/No): ").capitalize())
        if (criterio == "Si"):
            balcon = validar_si_no(input("¿Requiere  balcón? (Si/No): ").capitalize()) == "Si"
            criterios_elegidos['Balcon'] = balcon
    
        return criterios_elegidos
    
    # NUESTRO CHECK-IN 15:00, CHECK-OUT 11:00
    def hacer_reserva(self, Hotel):
        #hoy = datetime.date.today().strftime("%d/%m/%Y")
        hoy = datetime.now().strftime("%d/%m/%Y")

        # 1) Pregunto al cliente fecha check-in, fecha check-out
        check_in = validar_fecha_posteriori(hoy,validar_fecha(input('Ingrese la fecha deseada de check-in (dd/mm/aaaa): ')))
        check_out = validar_fecha_posteriori(check_in,validar_fecha(input('Ingrese la fecha deseada de check-out (dd/mm/aaaa): ')))
        
        # 2) Pregunto criterios de interes
        criterios_elegidos = self.recolectar_criterios_interes()
        
        # 3) Busco al empleado administrativo menos ocupado
        admin = Hotel.buscar_empleado(1)
        empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Administrativo')
        
        # 4) ¡¡¡ Chequear disponibilidad y asignacion de cuarto lo hace el personal administrativo !!
        
        """ debugging
        print(type(empleado))
        print(dir(empleado))  # Imprime los atributos y métodos de la instancia
        print(inspect.signature(empleado.disponibilidad_habitacion))

        print(Hotel.habitaciones)
        print(Hotel.reservas)
        print(check_in)
        print(check_out)
        print(criterios_elegidos)
        print(empleado)
        if isinstance(empleado, Empleado):
            habitacion = empleado.disponibilidad_habitacion(Hotel.habitaciones, Hotel.reservas, check_in, check_out, criterios_elegidos)
        else:
            print("El objeto empleado no es una instancia de la clase Empleado.")
        """


        habitacion = empleado.disponibilidad_habitacion(Hotel.habitaciones)#, Hotel.reservas, check_in, check_out, criterios_elegidos

        if (habitacion == None):
            print('No hay habitaciones disponibles en las fechas y criterios especificados')
        else:
            nueva_reserva = Reserva(self.mail, habitacion, check_in, check_out, hoy)
            print(f"Reserva realizada para la habitacion {habitacion.numero} del {check_in} al {check_out}")
            
            # Agregarlo a la lista de reservas del hotel reservas
            Hotel.reservas.append(nueva_reserva)
            
            # Agregar reserva a la lista reservas del cliente
            self.reservas.append(nueva_reserva)
    
    def ir_al_buffet(self, Hotel):
        reservas_activas = self.buscar_reservas_activas()
        if (len(reservas_activas) > 0):
            reserva = self.elegir_habitacion_activa(reservas_activas)
            
            opciones_comida = {
            'Desayuno': {'Huevos con tostadas': 900, 'Sandwhich': 1200, 'Cereales': 600},
            'Bebida': {'Agua': 600, 'Jugo': 700, 'Café': 800},
            'Refrigerio': {'Barrita': 300, 'Fruta': 300, 'Yogur': 500, 'Galleta': 400}}

            # 1) Crear pila con elecciones de buffet: tiene que elegir un desayuno, bebida, refrigerio en orden
            elecciones_comida = LifoQueue()
            
            for categoria, opciones in opciones_comida.items():
                preferencia = validar_opcion(input(f'Eliga una opcion de {categoria.lower()}: ').capitalize(), opciones)
                eleccion = (preferencia, opciones[preferencia])
                elecciones_comida.put(eleccion)
            
            # Le muestro su orden
            orden = ', '.join([f'{elemento[0]} (${elemento[1]})' for elemento in tuple(elecciones_comida)])
            print(f'Su orden de: {orden} fue efectuada correctamente')
            
            # Cobro la orden desde lo ultimo que agarro
            gastos = 0
            while (not elecciones_comida.empty()):
                precio = elecciones_comida.get()
                gastos += precio
            
            reserva.gastos_buffet += gastos
            
            # 2) asigno un empleado random de limpieza que haga limpieza en el buffet
            admin = Hotel.buscar_empleado(1)
            empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Limpieza')
            empleado.agregar_tarea_automatica(reserva.habitacion.numero, True)
        else:
            print('No esta permitido ir al buffet ya que no está hospedado en el hotel actualmente')

    def usar_el_minibar(self, Hotel):
        reservas_activas = self.buscar_reservas_activas()
        if (len(reservas_activas) > 0):
            reserva = self.elegir_habitacion_activa(reservas_activas)
            
            opciones_minibar = {'Coca-cola': 1000, 'Agua': 900, 'Alcohol': 2500, 'Snack': 300}
            
            preferencia = validar_opcion(input(f'Eliga una de las opciones del minibar: '), opciones_minibar.keys())
            
            reserva.gastos_minibar += opciones_minibar[preferencia]
            
            # 2) asigno un empleado de mantenimiento poco ocupado que reponga el minibar
            admin = Hotel.buscar_empleado(1)
            empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Mantenimiento')
            empleado.agregar_tarea_automatica(reserva.habitacion.numero)
        else:
            print('No esta permitido usar el minibar ya que no está hospedado en el hotel actualmente')
    
    def actualizar_gastado(self):
        self.gastado = 0
        hoy = datetime.now()
        for reserva in self.reservas:
            check_out_dt = datetime.strptime(reserva.check_out + ' 11:00', "%d/%m/%Y %H:%M")
            if (check_out_dt <= hoy):
                self.gastado += reserva.gastos_ocupacion + reserva.gastos_buffet + reserva.gastos_minibar
                
    def buscar_reservas_activas(self):
        reservas_activas = []
        for reserva in self.reservas:
            fecha_in = datetime.strptime(reserva.check_in + ' 11:00', "%d/%m/%Y %H_%M")
            fecha_out = datetime.strptime(reserva.check_out + ' 11:00', "%d/%m/%Y %H:%M")
            if (fecha_in <= datetime.today() <= fecha_out):
                reservas_activas.append(reserva)
        return reservas_activas
    
    def ver_reservas_activas(self):
        reservas_activas = self.buscar_reservas_activas()
        
        for reserva in reservas_activas:
            print(f"Reserva de habitación {reserva.habitacion.numero} del {reserva.check_in} al {reserva.check_out}\n"
                  f"Gastos en el buffet: ${reserva.gastos_buffet}\n"
                  f"Gastos en el minibar: ${reserva.gastos_minibar}\n"
                  f"Costo total de la reserva: ${reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos_ocupacion}")
            print()
            
    def elegir_habitacion_activa(self, reservas_activas):
        if (len(reservas_activas) > 1):
            habitaciones = []
            print(f'Usted tiene {len(reservas_activas)} reservas activas:')
            for reserva in reservas_activas:
                num = reserva.habitacion.numero
                habitaciones.append(num)
                print(f'Habitación: {num}')
            habitacion = int(validar_opcion(validar_num(input('Ingrese el numero de habitación para asociar el gasto: ')), habitaciones))
            for reserva in reservas_activas:
                if (reserva.habitacion.numero == habitacion):
                    return reserva
        else:
            return reservas_activas[0]