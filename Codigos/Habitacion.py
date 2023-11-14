from datetime import datetime

class Habitacion():
    def __init__(self, numero: int, precio: int, capacidad: int, tipo, banio_privado: str, balcon: str):
        self.numero = numero
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.banio_privado = banio_privado
        self.balcon = balcon
        self.ocupada = None

    # método que se actualice el atributo ocupada cada vez que se abra el menu --> fecha de hoy
    def actualizar_estado_ocupacion(self, reservas):
        fecha_hoy = datetime.now()
        for reserva in reservas:
            check_in_dt = datetime.strptime(reserva.check_in + ' 15:00', "%d/%m/%Y %H:%M")
            fecha_hs_liberacion = datetime.strptime(reserva.check_out + ' 15:00', "%d/%m/%Y %H:%M")
            if (reserva.habitacion.numero == self.numero and check_in_dt <= fecha_hoy <= fecha_hs_liberacion):  
                self.ocupada = True
                return
        self.ocupada = False
        return
                
        

"""
Informacion de habitaciones:

tipo        capacidad    precio    baño privado      balcon
Simple:         1          15k          no             no
Doble:          2          25k          no             no
Familiar:       4          40k          si             no
Suite:          2          90k          si             si
"""
