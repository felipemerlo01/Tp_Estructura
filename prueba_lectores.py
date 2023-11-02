import pandas as pd
from datetime import datetime


Clientes=[]
Habitaciones=[]
Reservas=[]

class Usuario:
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.dni = dni
        self.mail = mail
        self.contrasena = contrasena

class Cliente(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        #self.gastado=gastado #--> puse gastado pq saldo es como el saldo a favor que uno tiene ≠ a favor 
        self.reservas = [] 
        #si quiero poner los gastos por la habitacion y no por clientes 
        self.gastos_por_habitacion = {}  # Diccionario para llevar un registro de los gastos por habitación

class Administrador(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)

   
    def asignar_tareas(self, empleado, tareas):
            empleado.asignar_tareas(tareas)
            print(f"Tareas asignadas a {empleado.nombre} {empleado.apellido}: {tareas}")


    def dar_empleado_de_alta(self, empleado):
        self.empleados.append(empleado)
        empleado.actualizar_estado("Activo")  # Cambiar el estado del empleado a "Activo"
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de alta como empleado.")


    def dar_empleado_de_baja(self, empleado):
        empleado.actualizar_estado("Inactivo")  # Cambiar el estado del empleado a "Inactivo"
        self.empleados.remove(empleado)
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de baja como empleado.")
    #caos
    
class Empleado(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail: str, contrasena: str, legajo:int, rol: str):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.rol = rol
        self.registro_ingresos = []  # Lista para registrar los ingresos del empleado
        self.registro_egresos = []  # Lista para registrar los egresos del empleado
        # self.tareas = []  # Lista para almacenar las tareas asignadas
        self.estado = "Activo"  # Inicialmente, el empleado se encuentra activo
        #self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas

#Esta parte esta bien del codigo 

    def registro_ingreso(self):
        # Registrar la fecha y hora actual de ingreso
        fecha_actual = datetime.now()
        ingreso = {
            'fecha': fecha_actual.strftime('%Y-%m-%d'),
            'hora': fecha_actual.strftime('%H:%M:%S')}
        self.registro_ingresos.append(ingreso)

    def registro_egreso(self):
        # Registrar la fecha y hora actual de egreso
        fecha_actual = datetime.now()
        egreso = {
            'fecha': fecha_actual.strftime('%Y-%m-%d'),
            'hora': fecha_actual.strftime('%H:%M:%S')}
        self.registro_egresos.append(egreso)
    
    def realizar_check_in(self, habitacion):
        # Implementar lógica para realizar el check-in
        # Actualizar el estado de la habitación a "Ocupada"
        if habitacion.estado == "Disponible":
            fecha_actual = datetime.now()
            habitacion.estado = "Ocupada"
            habitacion.fecha_check_in = fecha_actual
            self.registro_ingreso()
            print(f"Check-in realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")

    def realizar_check_out(self, habitacion):
        # Implementar lógica para realizar el check-out
        # Actualizar el estado de la habitación a "Disponible"
        if habitacion.estado == "Ocupada":
            fecha_actual = datetime.now()
            habitacion.estado = "Disponible"
            habitacion.fecha_check_out = fecha_actual
            self.registro_egreso()
            print(f"Check-out realizado en la habitacion {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
    
    #aca va a aparecer el estado que tiene el empleado dependiendo de lo que decide el administrativo 

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    #aca se va a ver la tarea que tiene asiganda ese empleado
    def asignar_tareas(self, tareas):
        for tarea in tareas:
            self.tareas.put(tarea) #el empleado tiene un cola de tareas 

    def realizar_siguiente_tarea(self):
        if not self.tareas.empty():
            tarea = self.tareas.get()
            print(f"{self.nombre} {self.apellido} realizando tarea: {tarea}")

    def finalizar_tarea(self):
        # Implementar lógica de finalizar tarea de limpieza y mantenimiento
            pass
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.habitaciones = [] # podria ser lista enlazada
        self.reservas = []


class Habitacion():
    def __init__(self, numero, precio, capacidad, tipo, bano_privado, balcon):
        self.numero = numero #--> numero de habitación que tendría la reserva 
        self.precio = precio
        self.capacidad = capacidad
        self.tipo = tipo
        self.bano_privado = bano_privado
        self.balcon = balcon
        self.ocupada = False


class Reserva:
    def __init__(self, id, dni_cliente, habitacion: int, check_in: str, check_out: str, duracion:int):
        self.id = id
        self.dni_cliente = dni_cliente
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.duracion = duracion
        self.fecha_reserva = datetime.now()
        self.gastos = 0
        self.gastos_buffet = 0  # Gastos en el buffet relacionados con la reserva
        self.gastos_minibar = 0 

    def agregar_gastos_buffet(self, costo):
        self.gastos_buffet += costo

    def agregar_gastos_minibar(self, costo):
        self.gastos_minibar += costo

##############################################################################################################
usuarios = pd.read_csv('usuarios.csv')
reservas= pd.read_csv('reservas.csv')

hotel_prueba=Hotel("Los Pollos Hermanos")

for _, row in reservas.iterrows():
        nueva_reserva = Reserva(int(row["id"]),int(row["dni_cliente"]),int(row["numero_hab"]),row["Fecha_inicio"],row["Fecha_fin"],int(row["Duracion"]))
        hotel_prueba.reservas.append(nueva_reserva)

for _, row in usuarios.iterrows():
    if row["Rol"] == "Cliente":
        nuevo_usuario = Cliente(row["Nombre"],row["Apellido"],row["Fecha de Nacimiento"],row["Sexo"],row["dni"],row["mail"],row["contraseña"])
        hotel_prueba.usuarios.append(nuevo_usuario)
    elif row["Rol"] in ["Mantenimiento","Administrativo","Limpieza"]:
        nuevo_empleado = Empleado(row["Nombre"], row["Apellido"], row["Fecha de Nacimiento"],row["Sexo"],row["dni"],row["mail"],row["contraseña"], row["legajo"], row["Rol"])
        hotel_prueba.usuarios.append(nuevo_empleado)
    elif row["Rol"] == "Administrador":
        administrador = Administrador(row["Nombre"],row["Apellido"],row["Fecha de Nacimiento"],row["Sexo"],row["dni"],row["mail"],row["contraseña"])
        
#se
#todo ok. joya anda bien genial, queda habitaciones
 
for n in hotel_prueba.reservas:
    print (n.habitacion)
""" 
for n in hotel_prueba.usuarios:
    print (n.nombre) 
for n in hotel_prueba.habitaciones

for n in hotel_prueba.
"""



# lector_reservas = open("reservas.csv","r")
# reservas = pd.read_csv('reservas.csv')