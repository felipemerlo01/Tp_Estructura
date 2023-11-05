class Habitacion():
    def __init__(self, numero: int, precio: int, capacidad: int, tipo, banio_privado: str, balcon: str, ocupada: str):
        self.numero = numero
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.banio_privado = banio_privado
        self.balcon = balcon
        self.ocupada = ocupada

    # método que se actualice el atributo ocupada cada vez que se abra el menu --> fecha de hoy
  

"""
Informacion de habitaciones:

tipo        capacidad    precio    baño privado      balcon
Simple:         1          15k          no             no
Doble:          2          25k          no             no
Familiar:       4          40k          si             no
Suite:          2          90k          si             si
"""
