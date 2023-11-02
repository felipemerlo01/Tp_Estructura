class Habitacion():
    def __init__(self,tipo,numero) -> None:
        self.tipo=tipo
        #Verificar
        self.numero=numero
        if self.tipo=="Simple":
            self.precio=15000
        elif self.tipo=="Doble":
            self.precio=25000
        elif self.tipo=="Familiar":
            self.precio=40000
        else:
            self.precio=90000
    
    def obtener_tipo(self):
        return self.tipo
    
    def descripcion(self):
        if self.tipo=="1":
            print('Tipo: Simple, Capacidad para 1 persona, con baño y minibar incluido. Precio: $15.000.') 
        if self.tipo=="2":
            pass


"""
tipo        capacidad    precio    baño privado    jacuzzi   minibar   oficina   balcon
Simple:         1          15k      no                 no       si        no        no
Doble:          2          25k      no                 no       si        no        no
Familiar:       4          40k      si        no       si        no        no
Suite:          2          90k      si        si       si        si        si
"""

