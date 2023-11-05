from Cliente import Cliente
from Empleado import Empleado
from Funciones_extra import verificar_fecha_de_nacimiento, validar_fecha, verificar_dni, verificar_sexo, verificar_mail, verificar_contrasena

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
    
    # def calcular_porcentaje_ocupacion():
    #     pass

    # def calcular_porcentaje_ocupacion_x_tipo_habitacion():
    #     pass

    def actualizar_base_reservas():
        pass
    def actualizar_base_usuarios():
        pass
            

    