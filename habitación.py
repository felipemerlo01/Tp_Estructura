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


"""
tipo        capacidad    precio    baño    jacuzzi   minibar   oficina   balcon
Simple:         1          15k      si        no       si        no        no
Doble:          2          25k      si        no       si        no        no
Familiar:       4          40k      si        no       si        no        no
Suite:          2          90k      si        si       si        si        si

"""
