class Habitacion():
    def __init__(self, numero, precio, capacidad, tipo, banio_privado, balcon):
        self.numero = numero #--> numero de habitación que tendría la reserva 
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.banio_privado = banio_privado
        self.balcon = balcon
        self.ocupada = False
    
    ''' def obtener_tipo(self):
        return self.tipo'''
    
    #aca se usan los diccionarios 
    '''def calcular_precio(self):
        precios = {
            'Simple': 15000,
            'Doble': 25000,
            'Familiar': 40000,
            'Suite': 90000}
        return precios.get(self.tipo, 0)'''

    # método que se actualice el atributo ocupada según como se ejecut el menu 


    
    
"""
tipo        capacidad    precio    baño privado    jacuzzi   minibar   oficina   balcon
Simple:         1          15k      no                 no       si        no        no
Doble:          2          25k      no                 no       si        no        no
Familiar:       4          40k      si        no       si        no        no
Suite:          2          90k      si        si       si        si        si
"""
