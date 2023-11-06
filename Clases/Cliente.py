from Usuario import Usuario
from Empleado import Empleado
from Reserva import Reserva
from datetime import datetime
from Funciones_extra import validar_fecha, validar_fecha_posteriori, validar_si_no, validar_capacidad_min, validar_precio, validar_opcion
from queue import LifoQueue
    
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
        
        # ¡¡ NOTA !!: si quieren agregamos otro criterio
        return criterios_elegidos
    
    # NUESTRO CHECK-IN 15:00, CHECK-OUT 11:00
    def hacer_reserva(self, diccionario_habitaciones, lista_reservas, empleado: Empleado):
        hoy = datetime.date.today().strftime("%d/%m/%Y")
        
        # 1) Pregunto al cliente fecha check-in, fecha check-out
        check_in = validar_fecha_posteriori(validar_fecha(input('Ingrese la fecha deseada de check-in: ')), hoy)
        check_out = validar_fecha_posteriori(validar_fecha(input('Ingrese la fecha deseada de check-out: ')), check_in)
        
        # 2) Pregunto criterios de interes
        criterios_elegidos = self.recolectar_criterios_interes()
        
        # 3) ¡¡¡ Chequear disponibilidad y asignacion de cuarto lo hace el persoal administrativo !!
        # El tema aca es a que empleado ???, el que tenga la menor cantidad de tareas en su queue?
        # el primero de personal administrativo que encuentre cuando recorra la base?
        
        habitacion = empleado.disponibilidad_habitacion(diccionario_habitaciones, lista_reservas, check_in, check_out, criterios_elegidos)
        
        if (habitacion == None):
            print('No hay habitaciones disponibles en las fechas y criterios especificados')
        else:
            nueva_reserva = Reserva(self.mail, habitacion, check_in, check_out, hoy)
            print(f"Reserva realizada para la habitacion {habitacion.numero} del {check_in} al {check_out}")
            
            # Agregarlo a la lista de reservas del hotel reservas
            lista_reservas.append(nueva_reserva)
            
            # ¡¡¡ IMPORTANTE !!! Agregar a base de datos?
            # Metodo de HOTEL escribir a base csv Reservas
            
            # Agregar reserva a la lista reservas del cliente
            self.reservas.append(nueva_reserva)

    def ver_reservas_activas(self):
        for reserva in self.reservas:
            fecha_in = datetime.strptime(reserva.check_in, "%d/%m/%Y")
            fecha_out = datetime.strptime(reserva.check_out, "%d/%m/%Y")
            if (fecha_in <= datetime.date.today() <= fecha_out):
                print(f"Reserva de habitación {reserva.habitacion.numero} del {reserva.check_in} al {reserva.check_out}\n"
                      f"Gastos en el buffet: ${reserva.gastos_buffet}\n"
                      f"Gastos en el minibar: ${reserva.gastos_minibar}\n"
                      f"Costo total de la reserva: ${reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos_ocupacion}")
                print()
    
    def ir_al_buffet(self, reserva, Hotel):
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
        admin = Hotel.obtener_admin()
        empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Limpieza')
        empleado.agregar_tarea_automatica(reserva.habitacion.numero, True)

    def usar_el_minibar(self, reserva, Hotel):
        opciones_minibar = {'Coca-cola': 1000, 'Agua': 900, 'Alcohol': 2500, 'Snack': 300}
        
        preferencia = validar_opcion(input(f'Eliga una de las opciones del minibar: '), opciones_minibar.keys())
        
        reserva.gastos_minibar += opciones_minibar[preferencia]
        
        # 2) asigno un empleado random de mantenimiento que reponga el minibar
        admin = Hotel.obtener_admin()
        empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Mantenimiento')
        empleado.agregar_tarea_automatica(reserva.habitacion.numero)
    
    def actualizar_gastado(self):
        self.gastado = 0
        hoy = datetime.now()
        for reserva in self.reservas:
            check_out_dt = datetime.strptime(reserva.check_out + ' 11:00', "%d/%m/%Y %H:%M")
            if (check_out_dt <= hoy):
                self.gastado += reserva.gastos_ocupacion + reserva.gastos_buffet + reserva.gastos_minibar
            
    #hay que crear una tipo de categoria dependiendo del gasto del cliente pero puede que convenga hacer 
    def tipo_cliente(self):
        pass