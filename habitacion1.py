class Habitacion():
    def __init__(self, numero, precio, capacidad, tipo, bano_privado, ventana_balcon):
        self.numero = numero #--> numero de habitación que tendría la reserva 
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.bano_privado = bano_privado
        self.ventana_balcon = ventana_balcon
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

criterio = input("¿Desea filtrar por ventana balcón? (Sí/No): ")
if criterio.lower() == "sí":
    ventana_balcon = input("¿Requiere ventana balcón? (Sí/No): ").lower() == "sí"
    criterios_elegidos['ventana_balcon'] = ventana_balcon