from datetime import datetime
from queue import Queue, LifoQueue

#para mi hay que crear una clase que sea hotel tambien pero creo que en otra hoja para que empiece
# a quedar un poco más prolijo todo por el tema de generar todo los informes \
'''class hotel():
    def __init__(self,nombre):
         self.nombre=nombre 
         #habría que agregar mil cosas mas  
         pass

    def calcular_porcentaje_ocupacion():
        pass

    def calcular_porcentaje_ocupacion_x_tipo_habitacion():
        pass'''

#agarren lo que quieran de aca 
    
class Hotel():
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = [] # podria ser lista enlazada
        self.habitaciones = [] # podria ser lista enlazada
        self.ingresos = 0 # los gastos de las reservas se suman acá
        self.reservas = LifoQueue(maxsize=0)
        
    def suma_ingresos(self, reserva: Reserva):
        self.ingresos += reserva.gastos + reserva.habitacion.precio
    
    # def calcular_porcentaje_ocupacion():
    #     pass

    # def calcular_porcentaje_ocupacion_x_tipo_habitacion():
    #     pass
    
#creo una clase de reserva 
class Reserva:
    def __init__(self, habitacion, check_in, check_out):
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.fecha_reserva = datetime.now()
        self.gastos = 0

class Usuario():
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str,dni: int, mail, contrasena):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
        self.dni=dni
        self.mail=mail
        self.contrasena=contrasena

    #verificar dni 
    def verificar_dni(self):
    # El DNI es un número (int) de 8 dígitos
        return 10000000 <= self.dni <= 99999999
    
    #verificar sexo
    def verificar_sexo(self):
        if self.sexo not in ['M', 'F', 'f', 'm']:
            return False
        return True
    
    #verificar edad
    def verificar_edad(self):
        if self.edad < 18 or self.edad > 100:
            return False
        return True
    
    #verificar contrasena
    #aca no me esta verificando que tenga una longitud min
    def contrasena_fuerte(self):
    #puede ser que haya que borrar el self?   
        if len(self.contrasena) < 8:
            return False

        def contiene_numero():
            verifica = False
            for elemento in self.contrasena:
                if (ord(elemento) >= 48 and ord(elemento) <= 58):
                    verifica = True
            return verifica  

        def contiene_dos_mayusculas():
            contador = 0
            for elemento in self.contrasena:
                if (ord(elemento) >= 65 and ord(elemento) <= 90):
                    contador += 1

            if (contador >= 2):
                return True
            else:
                return False

        return contiene_numero() and contiene_dos_mayusculas()
    #se debe vincular con la reserva que tiene con el hotel !!!

#hay que poner el gasto de la habitacion directamente en la clase de la habitación 

class Cliente(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail, contrasena, gastado ):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.gastado=gastado #--> puse gastado pq saldo es como el saldo a favor que uno tiene ≠ a gasto
        self.reservas = [] 
        #si quiero poner los gastos por la habitacion y no por clientes 
        self.gastos_por_habitacion = {}  # Diccionario para llevar un registro de los gastos por habitación

    def hacer_reserva(self, habitacion, check_in, check_out):
        # calculo el costo y disponibilidad 
        if self.verificar_disponibilidad_habitacion(habitacion, check_in, check_out):
            costo_reserva = self.calcular_costo_reserva(habitacion, check_in, check_out)
            self.gastado -= costo_reserva
            self.registrar_gasto_por_habitacion(habitacion, costo_reserva)  # Registra el gasto por habitación
            # Crear la reserva
            reserva = Reserva(habitacion, check_in, check_out)
            self.reservas.append(reserva)
            print(f"Reserva realizada para la habitación {habitacion} del {check_in} al {check_out}")
        else:
            print("No se pudo realizar la reserva debido a falta de disponibilidad.")
    def ver_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva de habitación {reserva.habitacion} del {reserva.check_in} al {reserva.check_out}")  





 #esta es la parte que quieren que vaya directamente en la clase habitación    
    def ir_al_buffet(self, habitacion, costo_comida):
        if costo_comida > 0:
            print(f"Ha gastado ${costo_comida} en el buffet en la habitación {habitacion}.")
            self.gastado += costo_comida
            self.registrar_gasto_por_habitacion(habitacion, costo_comida)  # Registra el gasto por habitación
        else:
            print("No hay gastos en el buffet.")
#aca lo que se puede haceer es que se utiliza el costo de cada producto que se consumio o todo junto
    def usar_el_minibar(self, habitacion, costo_producto):
        if costo_producto > 0:
            print(f"Ha gastado ${costo_producto} en el minibar en la habitación {habitacion}.")
            self.gastado += costo_producto
            self.registrar_gasto_por_habitacion(habitacion, costo_producto)  # Registra el gasto por habitación
        else:
            print("No hay gastos en el minibar.")

    def registrar_gasto_por_habitacion(self, habitacion, costo):
        if habitacion in self.gastos_por_habitacion:
            self.gastos_por_habitacion[habitacion] += costo
        else:
            self.gastos_por_habitacion[habitacion] = costo

    def calcular_total_a_pagar(self):
        costo_reservas = sum(self.calcular_costo_reserva(reserva.habitacion, reserva.check_in, reserva.check_out) for reserva in self.reservas)
        # Calcular el gasto total en el buffet y minibar
        gasto_buffet = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "buffet" in habitacion.lower())
        gasto_minibar = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "minibar" in habitacion.lower())
        
        total_a_pagar = costo_reservas + gasto_buffet + gasto_minibar
        return total_a_pagar


    def ver_gastos_totales(self):
        total_a_pagar = self.calcular_total_a_pagar()
        gasto_buffet = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "buffet" in habitacion.lower())
        gasto_minibar = sum(gasto for habitacion, gasto in self.gastos_por_habitacion.items() if "minibar" in habitacion.lower())
        print(f"Total a pagar: ${total_a_pagar}")
        print(f"Gasto en el buffet: ${gasto_buffet}")
        print(f"Gasto en el minibar: ${gasto_minibar}")



    def verificar_disponibilidad_habitacion(self, habitacion, check_in, check_out):
        for reserva in self.reservas:
            if reserva.habitacion == habitacion:
                if (check_in >= reserva.check_in and check_in <= reserva.check_out) or (check_out >= reserva.check_in and check_out <= reserva.check_out):
                    return False  # La habitación ya está reservada para esas fechas
        return True  # La habitación está disponible

    def calcular_costo_reserva(self, habitacion, check_in, check_out):
        # lógica calcular el costo de la reserva
        pass

    #hay que crear una tipo de categoria dependiendo del gasto del cliente pero puede que convenga hacer 
    def tipo_cliente(self):
        pass



#gastos asociados a un cliente 
'''def ir_al_buffet(self, costo_comida):
        # Implementar lógica de ir al buffet y gastar
        if costo_comida > 0:
            print(f"Ha gastado ${costo_comida} en el buffet.")
            self.gastado += costo_comida
        else:
            print("No hay gastos en el buffet.")

    def usar_el_minibar(self, costo_producto):
        # Implementar lógica de usar el minibar y gastar
        if costo_producto > 0:
            print(f"Ha gastado ${costo_producto} en el minibar.")
            self.gastado += costo_producto
        else:
            print("No hay gastos.")
'''
 #puede tener + de una reserva el mismo cliente, es de esta froma que se crea como si yo te dijera un historial 
     

 #si quiero que los gastos se hagan por habitacion se hace así + habilatr la otra parte 


#esta parte del administrador esta ok 

class Administrador(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail, contrasena):
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

    
    
class Empleado(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail, contrasena, legajo:int):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
        self.registro_ingresos = []  # Lista para registrar los ingresos del empleado
        self.registro_egresos = []  # Lista para registrar los egresos del empleado
        # self.tareas = []  # Lista para almacenar las tareas asignadas
        self.estado = "Activo"  # Inicialmente, el empleado se encuentra activo
        self.tareas = Queue()  # Usar una cola para almacenar las tareas asignadas

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
            print(f"Check-in realizado en la habitación {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")

    def realizar_check_out(self, habitacion):
        # Implementar lógica para realizar el check-out
        # Actualizar el estado de la habitación a "Disponible"
        if habitacion.estado == "Ocupada":
            fecha_actual = datetime.now()
            habitacion.estado = "Disponible"
            habitacion.fecha_check_out = fecha_actual
            self.registro_egreso()
            print(f"Check-out realizado en la habitación {habitacion.numero} el {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
    
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

    
    
class Limpieza(Empleado):
        def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail, contrasena, legajo:int):
            super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena, legajo)
        
        def finalizar_tarea(self):
        # Implementar lógica de finalizar tarea de limpieza
            pass
       
    
class Mantenimiento(Empleado):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str, legajo:int):
         super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena, legajo)

    def finalizar_tarea(self):
        # Implementar lógica de finalizar tarea de mantenimiento 
        pass



""" 
Usuario -> Cliente
        -> Administrador  ¿que cosas hace?
        -> Empleado     Metodo (registrar_ingreso), Metodo(registrar_egreso)
                        --> Limpieza        --> Metodo (finaliizar_tarea) 
                        --> Mantenimiento    -> Metodo (finalizar_tarea)  
                        --> Administrativo   --> Metodo (asignar_tareas)

Cliente -> hacer_reserva, ir_al_buffet, usar_el_minibar

Administrativo -> check_in, check_out, hacer_reserva, asignar_tareas, ver_inventario_personal

Administrador -> dar_empleado_de_alta, dar_empleado_de_baja, sacar_la_basura xd

"""
'''# Ejemplo de uso
admin = Adminitrador("Admin", "Adminson", 35, "M", 123456789, "admin@example.com", "adminpass")
empleado = Empleado("Empleado", "Ejemplo", 25, "F", 987654321, "empleado@example.com", "empleadopass", 1001)

admin.dar_empleado_de_baja(empleado)  # El administrador da de baja al empleado y cambia su estado a "Inactivo"
print(f"Estado del empleado: {empleado.estado}")
En este ejemplo, el administrador puede dar de baja a un empleado y cambiar su estado a "Inactivo". El método dar_empleado_de_baja en Adminitrador llama al método actualizar_estado del empleado para realizar esta tarea. El estado del empleado se refleja y se puede consultar en cualquier momento.

'''





