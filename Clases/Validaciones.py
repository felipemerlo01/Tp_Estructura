from datetime import datetime
from re import fullmatch

# Funcion de validar fechas para uso general (no me parece que vaya como metodo de la clase): --> convendria ponerlo en un archivo de validaciones sueltas, poner ahi tambien las de hotel
# "Las funciones de validaciones generales pueden estar en un archivo aparte, el cuál se importará
# cuando fuera necesario."

def validar_fecha(fecha_ingresada):
    while (True):
        try:
            fec = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
            return fecha_ingresada
        except ValueError:
            fecha_ingresada = input('Ingrese un formato de fecha valido (dd/mm/YYYY): ')
            
def validar_check_out(fecha_check_in, fecha_check_out):
    while (True):
        check_in = datetime.strptime(fecha_check_in, '%d/%m/%Y')
        check_out = datetime.strptime(fecha_check_out, '%d/%m/%Y')

        cant_dias = (check_out - check_in).days

        if cant_dias >= 1:
            return fecha_check_out
        else:
            fecha_check_out = validar_fecha(input('Incorrecto. Ingrese una fecha posterior al check-in: '))
            
# valida fecha nacimiento
def verificar_fecha_de_nacimiento(fecha_de_nacimiento):
    while (True):
        fecnac = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
        hoy = datetime.date.today()
        edad = hoy.year - fecnac.year - ((hoy.month, hoy.day) < (fecnac.month, fecnac.day))

        if edad < 18:
            fecha_de_nacimiento = validar_fecha(input('Ingrese una fecha de nacimiento valida: '))
        else:
            return fecha_de_nacimiento
        
# verificar DNI
def verificar_dni(dni):
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
def verificar_sexo(sexo):
    while (sexo not in ['M', 'F']):
        sexo = input('Ingresar un sexo valido: ').upper()
    return sexo

# verifica formato mail
def verificar_mail(mail):
    formato = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    while (fullmatch(formato, mail) == False):
        mail = input('Ingrese un mail valido: ')
    return mail

# verificar contrasena
def verificar_contrasena(contrasena):
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
