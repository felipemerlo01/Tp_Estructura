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
        # self.gastos_por_habitacion = {}  # Diccionario para llevar un registro de los gastos por habitación

    def recolectar_criterios_interes(self):
        criterios_elegidos = {}
        # Asimismo hay que validarlos
        
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
                      f"Costo total de la reserva: ${reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos_ocupacion}") # reserva.gastos convendria que venga inicializada con el precio*dias creo
                print()
                
    
    def ir_al_buffet(self, reserva, Hotel):
        # 1) Crear pila con elecciones de buffet: tiene que elegir un desayuno, bebida, refrigerio
        
        opciones_comida = {
        'Desayuno': {'Huevos con tostadas': 900, 'Sandwhich': 1200, 'Cereales': 600},
        'Bebida': {'Agua': 600, 'Jugo': 700, 'Café': 800},
        'Refrigerio': {'Barrita': 300, 'Fruta': 300, 'Yogur': 500, 'Galleta': 400}}

        elecciones_comida = LifoQueue()
        
        for categoria, opciones in opciones_comida.items():
            preferencia = validar_opcion(input(f'Eliga una opcion de {categoria.lower()}: ').capitalize(), opciones)
            eleccion = opciones[preferencia]
            elecciones_comida.put(eleccion)
            
        print('Orden efectuada correctamente')
        
        gastos = 0
        while (not elecciones_comida.empty()):
            precio = elecciones_comida.get()
            gastos += precio
        
        reserva.gastos_buffet += gastos
        
        # 2) asigno un empleado random de limpieza que haga limpieza en el buffet
        admin = Hotel.obtener_admin()
        empleado = admin.asignar_empleado_menos_ocupado(Hotel.usuarios, 'Limpieza')
        empleado.agregar_tarea_automatica(reserva.habitacion.numero, False)

    def usar_el_minibar(self, reserva, costo_producto):
        if costo_producto > 0:
            reserva.agregar_gastos_minibar(costo_producto)
            print(f"Ha gastado ${costo_producto} en el minibar en la habitación {reserva.habitacion}.")
           
            
        else:
            print("No hay gastos en el minibar.")
        #si se consume en el minbar el administrador debe mandar a uno de mantenimiento a que lo reponga 
    
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

#esto de abajo vuela? ok
# nos parecieron medio innecesarias, quedarn en comentarios x las dudas ni idea

#gastos asociados a un cliente 
'''def ir_al_buffet(self, costo_comida):
        # Implementar lógica de ir al buffet y gastar
        if costo_comida > 0:
            print(f"Ha gastado ${costo_comida} en el buffet.")
            self.gastado += costo_comida
        else:
            print("No hay gastos en el buffet.")

    def usar_el_minibar(self, costo_producto):
        # Implementar lógica de usar el minibar y gastar
        if costo_producto > 0:
            print(f"Ha gastado ${costo_producto} en el minibar.")
            self.gastado += costo_producto
        else:
            print("No hay gastos.")
'''

# def hacer_reserva(self, empleado: Empleado, habitacion, check_in, check_out):
        
    #     # Calculo el costo y disponibilidad
    #     if self.verificar_disponibilidad_habitacion(habitacion, check_in, check_out):
    #         costo_reserva = self.calcular_costo_reserva(habitacion, check_in, check_out)
    #         #aca tengo gastado 
    #         self.gastado -= costo_reserva
    #         self.registrar_gasto_por_habitacion(habitacion, costo_reserva)  # Registra el gasto por habitación
    #         # Crear la reserva
    #         reserva = Reserva(habitacion, check_in, check_out)
    #         self.reservas.append(reserva)
    #         print(f"Reserva realizada para la habitacion {habitacion} del {check_in} al {check_out}")
    #     else:
    #         print("No se pudo realizar la reserva debido a falta de disponibilidad.")

'''def registrar_gasto_por_habitacion(self, habitacion, costo):
    if habitacion in self.gastos_por_habitacion:
        self.gastos_por_habitacion[habitacion] += costo
    else:
        self.gastos_por_habitacion[habitacion] = costo'''

'''def calcular_total_a_pagar(self):
    costo_reservas = sum(self.calcular_costo_reserva(reserva.habitacion, reserva.check_in, reserva.check_out) for reserva in self.reservas)
    # Calcular el gasto total en el buffet y minibar
    gasto_buffet = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "buffet" in habitacion.lower())
    gasto_minibar = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "minibar" in habitacion.lower())
    
    total_a_pagar = costo_reservas + gasto_buffet + gasto_minibar
    return total_a_pagar'''


'''def ver_gastos_totales(self):
    total_a_pagar = self.calcular_total_a_pagar()
    gasto_buffet = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "buffet" in habitacion.lower())
    gasto_minibar = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "minibar" in habitacion.lower())
    print(f"Total a pagar: ${total_a_pagar}")
    print(f"Gasto en el buffet: ${gasto_buffet}")
    print(f"Gasto en el minibar: ${gasto_minibar}")'''