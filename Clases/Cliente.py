from Usuario import Usuario
from Empleado import Empleado
from Reserva import Reserva
from datetime import datetime
from Hotel import Hotel
from Validaciones import validar_fecha, validar_check_out, validar_si_no, validar_capacidad_min, validar_precio
    
class Cliente(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.gastado = 0 
        self.reservas = []
        # self.gastos_por_habitacion = {}  # Diccionario para llevar un registro de los gastos por habitación

    def recolectar_criterios_interes(self):
        criterios_elegidos = {}
        # Hay que pedirle baño privado, capacidad, precio, y balcon
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
        
        # 1) Pregunto al cliente fecha check-in, fecha check-out
        check_in = validar_fecha(input('Ingrese la fecha deseada de check-in: '))
        check_out = validar_check_out(validar_fecha(input('Ingrese la fecha deseada de check-out: ')))
        
        # 2) Pregunto criterios de interes
        criterios_elegidos = self.recolectar_criterios_interes()
        
        # 3) ¡¡¡ Chequear disponibilidad y asignacion de cuarto lo hace el persoal administrativo !!
        # El tema aca es a que empleado ???, el que tenga la menor cantidad de tareas en su queue?
        # el primero de personal administrativo que encuentre cuando recorra la base?
        
        habitacion = empleado.disponibilidad_habitacion(diccionario_habitaciones, lista_reservas, check_in, check_out, criterios_elegidos)
        
        if (habitacion == None):
            print('No hay habitaciones disponibles en las fechas y criterios especificados')
        else:
            nueva_reserva = Reserva(habitacion, check_in, check_out, datetime.date.today())
            print('Se creó la reserva correctamente!')
            
            # Agregarlo a la lista de reservas del hotel reservas
            lista_reservas.append(nueva_reserva)
            
            # ¡¡¡ IMPORTANTE !!! Agregar a base de datos?
            # Metodo de HOTEL escribir a base csv Reservas
            
            # Agrega costo de reserva a los gastos totales del cliente
            self.gastado += nueva_reserva.calcular_costo_reserva()
            
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
                      f"Costo total de la reserva: ${reserva.gastos_buffet + reserva.gastos_minibar + reserva.gastos}") # reserva.gastos convendria que venga inicializada con el precio*dias creo
                print()
                
    #esta es la parte que quieren que vaya directamente en la clase habitación    
    def ir_al_buffet(self, reserva, costo_comida):
            if costo_comida > 0:
                reserva.agregar_gastos_buffet(costo_comida)
                print(f"Ha gastado ${costo_comida} en el buffet en la habitación {reserva.habitacion.numero}.")
            else:
                print("No hay gastos en el buffet.")


    #aca lo que se puede haceer es que se utiliza el costo de cada producto que se consumio o todo junto
    def usar_el_minibar(self, reserva, costo_producto):
        if costo_producto > 0:
            reserva.agregar_gastos_minibar(costo_producto)
            print(f"Ha gastado ${costo_producto} en el minibar en la habitación {reserva.habitacion}.")
        else:
            print("No hay gastos en el minibar.")

    #hay que crear una tipo de categoria dependiendo del gasto del cliente pero puede que convenga hacer 
    def tipo_cliente(self):
        pass



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