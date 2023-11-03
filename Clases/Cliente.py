from Usuario import Usuario
from Empleado import Empleado
from Reserva import Reserva
from datetime import datetime
from Validaciones import validar_fecha, validar_check_out
    
class Cliente(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.gastado = 0 #--> puse gastado pq saldo es como el saldo a favor que uno tiene ≠ a favor 
        self.reservas = [] 
        self.gastos_por_habitacion = {}  # Diccionario para llevar un registro de los gastos por habitación

    def criterios_interes(self):
        
    
    # NUESTRO CHECK-IN 15:00, CHECK-OUT 11:00
    def hacer_reserva(self, empleado: Empleado):
        
        # Pregunto al cliente fecha check-in, fecha check-out
        check_in = validar_fecha(input('Ingrese la fecha deseada de check-in: ')) + ' 15:00'
        check_out = validar_check_out(validar_fecha(input('Ingrese la fecha deseada de check-out: '))) + ' 11:00'
        
        # Pregunto criterios de interes
        
        
        # Calculo el costo y disponibilidad
        if self.verificar_disponibilidad_habitacion(habitacion, check_in, check_out):
            costo_reserva = self.calcular_costo_reserva(habitacion, check_in, check_out)
            #aca tengo gastado 
            self.gastado -= costo_reserva
            self.registrar_gasto_por_habitacion(habitacion, costo_reserva)  # Registra el gasto por habitación
            # Crear la reserva
            reserva = Reserva(habitacion, check_in, check_out)
            self.reservas.append(reserva)
            print(f"Reserva realizada para la habitacion {habitacion} del {check_in} al {check_out}")
        else:
            print("No se pudo realizar la reserva debido a falta de disponibilidad.")

    def hacer_reserva(self, empleado: Empleado, habitacion, check_in, check_out):
        
        # Calculo el costo y disponibilidad
        if self.verificar_disponibilidad_habitacion(habitacion, check_in, check_out):
            costo_reserva = self.calcular_costo_reserva(habitacion, check_in, check_out)
            #aca tengo gastado 
            self.gastado -= costo_reserva
            self.registrar_gasto_por_habitacion(habitacion, costo_reserva)  # Registra el gasto por habitación
            # Crear la reserva
            reserva = Reserva(habitacion, check_in, check_out)
            self.reservas.append(reserva)
            print(f"Reserva realizada para la habitacion {habitacion} del {check_in} al {check_out}")
        else:
            print("No se pudo realizar la reserva debido a falta de disponibilidad.")

    def ver_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva de habitación {reserva.habitacion} del {reserva.check_in} al {reserva.check_out}")
            print(f"Gastos en el buffet: ${reserva.gastos_buffet}")
            print(f"Gastos en el minibar: ${reserva.gastos_minibar}")
            print(f"Costo total de la reserva: ${reserva.calcular_costo_total_reserva()}")



 #esta es la parte que quieren que vaya directamente en la clase habitación    
    def ir_al_buffet(self, reserva, costo_comida):
            if costo_comida > 0:
                reserva.agregar_gastos_buffet(costo_comida)
                print(f"Ha gastado ${costo_comida} en el buffet en la habitación {reserva.habitacion}.")
            else:
                print("No hay gastos en el buffet.")


#aca lo que se puede haceer es que se utiliza el costo de cada producto que se consumio o todo junto
    def usar_el_minibar(self, reserva, costo_producto):
        if costo_producto > 0:
            reserva.agregar_gastos_minibar(costo_producto)
            print(f"Ha gastado ${costo_producto} en el minibar en la habitación {reserva.habitacion}.")
        else:
            print("No hay gastos en el minibar.")

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



    def verificar_disponibilidad_habitacion(self, habitacion, check_in, check_out):
        for reserva in self.reservas:
            if reserva.habitacion == habitacion:
                if (check_in >= reserva.check_in and check_in <= reserva.check_out) or (check_out >= reserva.check_in and check_out <= reserva.check_out):
                    return False  # La habitación ya está reservada para esas fechas
        return True  # La habitación está disponible

    def calcular_costo_reserva(self, habitacion, check_in, check_out):
        # lógica calcular el costo de la reserva
        pass

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
 #puede tener + de una reserva el mismo cliente, es de esta froma que se crea como si yo te dijera un historial 
     

 #si quiero que los gastos se hagan por habitacion se hace así + habilatr la otra parte 