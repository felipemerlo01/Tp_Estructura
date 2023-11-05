from Cliente import Cliente
from Empleado import Empleado
from Funciones_extra import verificar_fecha_de_nacimiento, validar_fecha, verificar_dni, verificar_sexo, verificar_mail, verificar_contrasena
from datetime import datetime, date

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {}
        self.habitaciones = {}
        self.reservas = []
        
    def crear_usuario(self, opcion):
        nombre = input('Ingrese su nombre: ').capitalize()
        
        apellido = input('Ingrese su apellido: ').capitalize()

        fecha_de_nacimiento = verificar_fecha_de_nacimiento(validar_fecha(input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")))
        
        sexo = verificar_sexo(input("Ingrese su sexo (F/M): ").upper())
        
        dni = verificar_dni(input("Ingrese su DNI: "))
        
        mail = self.verificar_mail_existente(verificar_mail(input("Ingrese su mail: ")))
        
        contrasena = verificar_contrasena(input("Ingrese una nueva contraseña. Debe contener al menos 8 caracteres, con un mínimo de 2 mayúsculas y 2 numeros: "))
        
        if (opcion == '1'):
            nuevo_cliente = Cliente(nombre, apellido, fecha_de_nacimiento, sexo, int(dni), mail, contrasena)
            self.usuarios[nuevo_cliente.mail] = nuevo_cliente
            print(f'Se ha creado el usuario de {nuevo_cliente.nombre} {nuevo_cliente.apellido} correctamente')
            return nuevo_cliente
        elif (opcion == '2'):
            rol = self.verificar_rol(input("Ingrese su rol: "))
            legajo = self.crear_legajo
            
            nuevo_empleado = Empleado(nombre, apellido, fecha_de_nacimiento, sexo, int(dni), mail, contrasena, int(legajo), rol)
            self.usuarios[nuevo_empleado.mail] = nuevo_empleado
            print(f'Se ha creado el usuario de {nuevo_empleado.nombre} {nuevo_empleado.apellido} correctamente')
            return nuevo_empleado
    
    # verificar si el mail ya existe
    def verificar_mail_existente(self, mail: str):
        while (mail in self.usuarios): 
            mail = self.verificar_mail(input('Mail ya existente. Ingrese otro mail: '))
        return mail
    
    # verificar rol 
    def verificar_rol(self, rol: str):
        while rol not in ["Administrativo", "Mantenimiento", "Limpieza"]:
            rol = input("Rol invalido. Ingrese un rol valido: ")
        return rol

    # Buscar al ultimo usuario que tiene legajo y al nuevo usuario agregarle el siguiente legajo 
    def crear_legajo(self): 
        for usuario in reversed(self.usuarios.values()):
            if hasattr(usuario, 'legajo'):
                nuevo_legajo = usuario.legajo + 1
                return nuevo_legajo
            
    # valido el mail y contrasena al iniciar sesión
    def validar_inicio_sesion(self, mail: str, contrasena: str): 
        while (mail not in self.usuarios):
            mail = verificar_mail(input('Mail no encontrado. Ingrese un mail registrado: '))
        
        while (contrasena != self.usuarios[mail].contrasena):
            contrasena = input('Contraseña incorrecta. Ingrese nuevamente: ')
        
        return self.usuarios[mail]
    
    def iniciar_sesion(self):
        mail = verificar_mail(input('Ingrese su mail: '))
        contrasena = input('Ingrese su contraseña: ')
        
        return self.validar_inicio_sesion(mail, contrasena)
    
    def obtener_admin(self):
        for usuario in self.usuarios.values():
            if (hasattr(usuario, 'legajo') and usuario.legajo == 1):
                return usuario
    
    def procentaje_de_ocupacion(self):
        capacidad_total = len(self.habitaciones)
        capacidad_ocupada = 0
        for habitacion in self.habitaciones.values():
            if habitacion.ocupada == True:
                capacidad_ocupada += 1
        #actualizar txt
        print(f'El porcentaje actual de ocupación del hotel es del {(capacidad_ocupada/capacidad_total)*100}%')
        return

    def procentaje_de_ocupacion_por_tipo_de_habitación(self):   #hacemos que el admin pregunte el tipo?
        capacidad_total=len(self.habitaciones)
        tipos=["Simple","Doble","Familiar","Suite"]
        for tipo in tipos:
            ocupacion_del_tipo=0
            for habitacion in self.habitaciones.values():
                if habitacion.ocupada == True and habitacion.tipo == tipo:
                    ocupacion_del_tipo+=1
        # actualizar txt
            print(f"La ocupación de las habitaciones de tipo {tipo} es del {(ocupacion_del_tipo/capacidad_total)*100}% \n")
        return
    
    def calcular_ganacia_del_dia(self):
        ingreso_del_dia = 0
        for reserva in self.reservas:
            if reserva.check_out == datetime.today():
                ingreso_del_dia += (reserva.gastos_ocupacion + reserva.gastos_buffet + reserva.gastos_minibar)
        #actualizar txt
        return 
    
    # def cantidad_de_clientes_por_tipo(self):
    #     categorias = {'raton'}
        
    #     Cant_clientes_por_cat={}
        
    #     xd

    def buscar_empleado(self, nombre, apellido):
        for usuario in self.usuarios:
            if (hasattr(usuario, 'legajo') and nombre == usuario.nombre and apellido == usuario.apellido):
                return usuario
        return

    def validar_inicio_sesion(self, mail: str, contrasena: str): 
        while (mail not in self.usuarios):
            mail = verificar_mail(input('Mail no encontrado. Ingrese un mail registrado: '))
        
        while (contrasena != self.usuarios[mail].contrasena):
            contrasena = input('Contraseña incorrecta. Ingrese nuevamente: ')
        
        return self.usuarios[mail]

    #Actualizo el CSV de reservas con una nueva linea con la nueva reserva
    def actualizar_base_reservas(reserva, path):
        info_reserva = f"{reserva.mail_usuario},{reserva.habitacion.numero},{reserva.check_in},{reserva.check_out},{reserva.fecha_reserva}\n"
        with open(path,"a",newline='') as archivo_reservas:
            archivo_reservas.write(info_reserva)

    #Actualizo el CSV de usuarios con una nueva linea con el nuevo usuario
    def actualizar_base_usuarios(usuario, path):
        info_usuarios = f"{usuario.nombre},{usuario.apellido},{usuario.fecha_de_nacimiento},{usuario.sexo},{usuario.dni},{usuario.mail},{usuario.contrasena}\n"
        with open(path,"a",newline='') as archivo_usuarios:
            archivo_usuarios.write(info_usuarios)

    def actualizar_estado_habitaciones(self):
        for habitacion in self.habitaciones.values():
            habitacion.actualizar_estado_ocupacion(self.reservas)
    
    def actualizar_gasto_clientes(self):
        for usuario in self.usuarios.values():
            #Entra solo si es cliente, que no tiene el atributo legajo
            if (not hasattr(usuario, 'legajo')):
                usuario.actualizar_gastado()
    
    def actualizar_datos_totales(self):
        #Ejecuta todos los metodos de actualizaciones
        self.actualizar_estado_habitaciones()
        self.actualizar_gasto_clientes()
        
    
            

    