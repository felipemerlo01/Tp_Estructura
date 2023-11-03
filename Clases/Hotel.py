from datetime import datetime
from re import fullmatch
from queue import LifoQueue
from Cliente import Cliente
from Empleado import Empleado

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

        fecha_de_nacimiento = self.verificar_fecha_de_nacimiento(input("Ingrese su fecha de nacimiento (dd/mm/aaaa): "))
        
        sexo = self.verificar_sexo(input("Ingrese su sexo (F/M): ").upper())
        
        dni = self.verificar_dni(input("Ingrese su DNI: "))
        
        mail = self.verificar_mail_existente(self.verificar_mail(input("Ingrese su mail: ")))
        
        contrasena = self.verificar_contrasena(input("Ingrese una nueva contraseña. Debe contener al menos 8 caracteres, con un mínimo de 2 mayúsculas y 2 numeros: "))
        
        if (opcion == '1'):
            nuevo_cliente = Cliente(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
            self.usuarios.append(nuevo_cliente)
        elif (opcion == '2'):
            rol = self.verificar_rol(input("Ingrese su rol: "))
            legajo = int(self.crear_legajo)
            
            nuevo_empleado = Empleado(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena, legajo, rol)
            self.usuarios.append(nuevo_empleado)

    # verificar DNI
    def verificar_dni(self, dni: str):
        dni_valido = False
        while (dni_valido == False):
            try:
                int(dni)
                while (dni > 99999999 or dni < 10000000):
                    dni = int(input('Ingrese un DNI valido: '))
                return dni
            except:
                dni = input('Ingrese un DNI valido: ')
    
    # verificar sexo
    def verificar_sexo(self, sexo: str):
        while (sexo not in ['M', 'F']):
            sexo = input('Ingresar un sexo valido: ').upper()
        return sexo
    
    # verifica formato mail
    def verificar_mail(self, mail: str):
        formato = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        while (fullmatch(formato, mail) == False):
            mail = input('Ingrese un mail valido: ')
        return mail
    
    # valida fecha nacimiento
    def verificar_fecha_de_nacimiento(self, fecha_de_nacimiento: str):
        fec_valida = False
        while (fec_valida == False):
            try:
                fecnac = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
                hoy = datetime.date.today()
                edad = hoy.year - fecnac.year - ((hoy.month, hoy.day) < (fecnac.month, fecnac.day))

                if edad < 18:
                    fecha_de_nacimiento = input('Ingrese una fecha de nacimiento valida: ')
                else:
                    return fecha_de_nacimiento
            except ValueError:
                fecha_de_nacimiento = input('Ingrese un formato de fecha valido (dd/mm/YYYY): ')
    
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

    # verificar contrasena
    def verificar_contrasena(self, contrasena: str):
        valida = False
        while (valida == False): 
            numeros = 0
            mayusculas = 0
            caracteres = 0

            for elemento in contrasena:
                if (ord(elemento) >= 48 and ord(elemento) < 58): # numeros
                    numeros +=1
                if (ord(elemento) >= 65 and ord(elemento) <= 90): # mayusculas
                    mayusculas += 1
                caracteres +=1
            
            if (numeros < 2 or mayusculas < 2 or caracteres < 8):
                contrasena = input("Contrasena Invalida. Ingrese una contrasena valida: ")
            else:
                valida = True
                
        return contrasena
    
    # verificar rol 
    def verificar_rol(self, rol: str):
        while rol not in ["Administrativo", "Mantenimiento", "Limpieza"]:
            rol = input("Rol invalido. Ingrese un rol valido: ")
        return rol

    #aca lo que buscmos hacer es buscar al ultimo usuario que tiene legajo y a el nuevo usuario agregarle el siguiente legajo 
    def crear_legajo(self):
        i = -1
        while (i > -len(self.usuarios)): #ESTA FORMA DE RECORRER LA LISTA ESTA BUIEN 
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
            mail = self.verificar_mail(input('Mail no encontrado. Ingrese un mail registrado: '))
    
    def iniciar_sesion(self):
        mail = self.verificar_mail(input('Ingrese su mail: '))
        contrasena = input('Ingrese su contraseña: ')
        
        return self.validar_inicio_sesion(mail, contrasena)
            
            

    