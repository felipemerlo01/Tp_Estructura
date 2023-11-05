from Habitacion import Habitacion
from datetime import datetime

class Reserva:
    def __init__(self, habitacion: Habitacion, check_in: str, check_out: str, fecha_reserva = datetime.date.today()):
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.fecha_reserva = fecha_reserva
        self.gastos = 0
        self.gastos_buffet = 0  # Gastos en el buffet relacionados con la reserva
        self.gastos_minibar = 0 

    def agregar_gastos_buffet(self, costo):
        self.gastos_buffet += costo

    def agregar_gastos_minibar(self, costo):
        self.gastos_minibar += costo

    def calcular_costo_reserva(self):
        dias = (datetime.strptime(self.check_out, "%d/%m/%Y")-datetime.strptime(self.check_in, "%d/%m/%Y")).days
        costo_total = dias * self.habitacion.precio
        return costo_total
        