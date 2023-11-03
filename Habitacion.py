class Habitacion():
    def __init__(self, numero, precio, capacidad, tipo, bano_privado, balcon):
        self.numero = numero #--> numero de habitación que tendría la reserva 
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.bano_privado = bano_privado
        self.balcon = balcon
        self.ocupada = False
    
    def obtener_tipo(self):
        return self.tipo
    
    #aca se usan los diccionarios 
    def calcular_precio(self):
        precios = {
            'Simple': 15000,
            'Doble': 25000,
            'Familiar': 40000,
            'Suite': 90000}
        return precios.get(self.tipo, 0)

    #falta el def str 

habitaciones=[]

#mostrar las habitaciones disponibles 

def habitaciones_disponibles(habitaciones, criterios):
    pass
criterios_elegidos = {}

criterio = input("¿Desea filtrar por capacidad? (Sí/No): ")
if criterio.lower() == "sí":
    capacidad_minima = int(input("Capacidad mínima deseada: "))
    criterios_elegidos['capacidad'] = capacidad_minima

criterio = input("¿Desea filtrar por tipo? (Sí/No): ")
if criterio.lower() == "sí":
    tipo_elegido = input("Tipo de habitación deseado (Simple/Doble/Familiar/Suite): ")
    criterios_elegidos['tipo'] = tipo_elegido

criterio = input("¿Desea filtrar por baño privado? (Sí/No): ")
if criterio.lower() == "sí":
    bano_privado = input("¿Requiere baño privado? (Sí/No): ").lower() == "sí"
    criterios_elegidos['bano_privado'] = bano_privado

criterio = input("¿Desea filtrar por  balcón? (Sí/No): ")
if criterio.lower() == "sí":
    balcon = input("¿Requiere  balcón? (Sí/No): ").lower() == "sí"
    criterios_elegidos['balcon'] = balcon
    
    
"""
tipo        capacidad    precio    baño privado    jacuzzi   minibar   oficina   balcon
Simple:         1          15k      no                 no       si        no        no
Doble:          2          25k      no                 no       si        no        no
Familiar:       4          40k      si        no       si        no        no
Suite:          2          90k      si        si       si        si        si
"""
