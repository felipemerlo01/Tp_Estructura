from Habitacion import Habitacion
from datetime import datetime

class Reserva:
    def __init__(self, habitacion: Habitacion, check_in: str, check_out: str):
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.fecha_reserva = datetime.now()
        self.gastos = 0
        self.gastos_buffet = 0  # Gastos en el buffet relacionados con la reserva
        self.gastos_minibar = 0 

    def agregar_gastos_buffet(self, costo):
        self.gastos_buffet += costo

    def agregar_gastos_minibar(self, costo):
        self.gastos_minibar += costo