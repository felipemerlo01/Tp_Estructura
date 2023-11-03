from queue import LifoQueue
from Cliente import Cliente
from Empleado import Empleado
from Validaciones import verificar_fecha_de_nacimiento, validar_fecha, verificar_dni, verificar_sexo, verificar_mail, verificar_contrasena

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.habitaciones = [] 
        self.reservas = LifoQueue(maxsize=0)
        
    # def calcular_porcentaje_ocupacion():
    #     pass

    # def calcular_porcentaje_ocupacion_x_tipo_habitacion():
    #     pass
        
    def crear_usuario(self, opcion):
        nombre = input('Ingrese su nombre: ').capitalize()
        
        apellido = input('Ingrese su apellido: ').capitalize()

        fecha_de_nacimiento = verificar_fecha_de_nacimiento(validar_fecha(input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")))
        
        sexo = verificar_sexo(input("Ingrese su sexo (F/M): ").upper())
        
        dni = verificar_dni(input("Ingrese su DNI: "))
        
        mail = self.verificar_mail_existente(verificar_mail(input("Ingrese su mail: ")))
        
        contrasena = verificar_contrasena(input("Ingrese una nueva contraseña. Debe contener al menos 8 caracteres, con un mínimo de 2 mayúsculas y 2 numeros: "))
        
        if (opcion == '1'):
            nuevo_cliente = Cliente(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
            self.usuarios.append(nuevo_cliente)
        elif (opcion == '2'):
            rol = self.verificar_rol(input("Ingrese su rol: "))
            legajo = int(self.crear_legajo)
            
            nuevo_empleado = Empleado(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena, legajo, rol)
            self.usuarios.append(nuevo_empleado)
    
    # verificar si el mail ya existe
    def verificar_mail_existente(self, mail: str):
        mail_valido = False
        while (mail_valido == False):
            mail_valido = True
            for usuario in self.usuarios:
                if (usuario.mail == mail):
                    mail_valido = False
                    mail = self.verificar_mail(input('Mail ya existente. Ingrese otro mail: '))
                    break
        return mail     
    
    # verificar rol 
    def verificar_rol(self, rol: str):
        while rol not in ["Administrativo", "Mantenimiento", "Limpieza"]:
            rol = input("Rol invalido. Ingrese un rol valido: ")
        return rol

    # Buscar al ultimo usuario que tiene legajo y al nuevo usuario agregarle el siguiente legajo 
    def crear_legajo(self):
        i = -1
        while (i > -len(self.usuarios)): 
            if hasattr(self.usuarios[i], 'legajo'):
                nuevo_legajo = self.usuarios[i].legajo + 1
                return nuevo_legajo
            i -= 1
    
    # valido el mail y contrasena al iniciar sesión
    def validar_inicio_sesion(self, mail: str, contrasena: str):
        while (True):
            for usuario in self.usuarios:
                if (usuario.mail == mail):
                    while (True):
                        if (usuario.contrasena == contrasena):
                            return usuario
                        else:
                            contrasena = input('Contraseña incorrecta. Ingrese nuevamente: ')
            mail = verificar_mail(input('Mail no encontrado. Ingrese un mail registrado: '))
    
    def iniciar_sesion(self):
        mail = verificar_mail(input('Ingrese su mail: '))
        contrasena = input('Ingrese su contraseña: ')
        
        return self.validar_inicio_sesion(mail, contrasena)
            
            

    