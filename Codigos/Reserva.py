from datetime import date

class Reserva:
    def __init__(self, mail_usuario: str, num_habitacion:int, check_in: str, check_out: str, fecha_reserva = None, gastos_buffet = 0, gastos_minibar = 0):
        self.mail_usuario = mail_usuario
        self.num_hab = num_habitacion
        self.habitacion = None
        self.check_in = check_in
        self.check_out = check_out
        if fecha_reserva is None:
            fecha_reserva = date.today().strftime("%d/%m/%Y")
        self.fecha_reserva = fecha_reserva
        self.gastos_ocupacion = None
        self.gastos_buffet = gastos_buffet
        self.gastos_minibar = gastos_minibar
        

# la reserva va a guardar el num de habitacion