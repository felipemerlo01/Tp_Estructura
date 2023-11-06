from Habitacion import Habitacion
from datetime import datetime

class Reserva:
    def __init__(self, mail_usuario: str, habitacion: Habitacion, check_in: str, check_out: str, fecha_reserva = None, gastos_buffet = 0, gastos_minibar = 0):
        self.mail_usuario = mail_usuario
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        if fecha_reserva is None:
            fecha_reserva = datetime.date.today().strftime("%d/%m/%Y")
        self.fecha_reserva = fecha_reserva
        self.gastos_ocupacion = (datetime.strptime(self.check_out, "%d/%m/%Y")-datetime.strptime(self.check_in, "%d/%m/%Y")).days * self.habitacion.precio
        self.gastos_buffet = gastos_buffet
        self.gastos_minibar = gastos_minibar
        
    