from datetime import datetime, date
from re import fullmatch

# Funcion de validar fechas para uso general (no me parece que vaya como metodo de la clase): --> convendria ponerlo en un archivo de validaciones sueltas, poner ahi tambien las de hotel
# "Las funciones de validaciones generales pueden estar en un archivo aparte, el cuál se importará
# cuando fuera necesario."

def validar_fecha(fecha_ingresada):
    while (True):
        try:
            datetime.strptime(fecha_ingresada, "%d/%m/%Y")
            print()
            return fecha_ingresada
        except ValueError:
            fecha_ingresada = input('Ingrese un formato de fecha valido (dd/mm/YYYY): ')
            
def validar_fecha_posteriori(fecha_antes, fecha_despues):
    while (True):
        fecha_ant = datetime.strptime(fecha_antes, '%d/%m/%Y')
        fecha_des = datetime.strptime(fecha_despues, '%d/%m/%Y')       
    
        if (fecha_des > fecha_ant):
            print()
            return fecha_despues
        else:
            fecha_despues = validar_fecha(input('Incorrecto. Ingrese una fecha posterior: '))
            
# valida fecha nacimiento
def verificar_fecha_de_nacimiento(fecha_de_nacimiento):
    while (True):
        fecnac = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
        hoy = date.today()
        edad = hoy.year - fecnac.year - ((hoy.month, hoy.day) < (fecnac.month, fecnac.day))

        if edad < 18:
            fecha_de_nacimiento = validar_fecha(input('Ingrese una fecha de nacimiento valida: '))
        else:
            return fecha_de_nacimiento

# verificar DNI
def verificar_dni(dni):
    while (True):
        try:
            while (int(dni) > 99999999 or int(dni) < 10000000):
                dni = input('Ingrese un DNI valido: ')
            print()
            return dni
        except ValueError:
            dni = input('Ingrese un DNI valido: ')
            
# verificar sexo
def verificar_sexo(sexo):
    while (sexo not in ('M', 'F')):
        sexo = input('Ingresar un sexo valido: ').upper()
    print()
    return sexo

# verifica formato mail
def verificar_mail(mail):
    formato = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    while (fullmatch(formato, mail) is None):
        mail = input('Ingrese un mail valido: ')
    print()
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
    
    print()        
    return contrasena

def validar_num(numero):
    while (True):
        try:
            int(numero)
            print()
            return numero
        except:
            numero = input('Por favor, ingrese un número: ')

def validar_si_no(opcion):
    while (opcion not in ('Si', 'No')):
        opcion = input('Ingrese una opción valida (Si/No): ').capitalize()
    print()
    return opcion

def validar_precio(precio):
    while (True):
        try:
            while (int(precio) < 1):
                precio = input('Ingrese un precio máximo valido: ')
            print()
            return precio
        except ValueError:
            precio = input('Ingrese un precio máximo valido: ')
    
def validar_capacidad_min(capacidad):
    while (True):
        try:
            while (int(capacidad) < 1  or int(capacidad) > 4):
                capacidad = input('Ingrese una de las capacidades disponibles: ')
            print()
            return capacidad
        except ValueError:
            capacidad = input('Ingrese una capacidad válida: ')
            
def validar_opcion(opcion_elegida, opciones_disponibles):
    while (opcion_elegida not in opciones_disponibles):
        opcion_elegida = input('Eliga una de las opciones presentadas: ').capitalize()
    print()
    return opcion_elegida

#########################

def menu_principal():
    print('''Bienvenido al menu:
1. Iniciar sesión
2. Registrar usuario
3. Salir\n''')
    
def menu_registro():
    print('''1. Registrarse como cliente
2. Registrarse como empleado
3. Volver\n''')
    
def validar_opcion_menu(opcion, cantidad_opciones):
    while (True):
        try:
            while (not (1 <= int(opcion) <= cantidad_opciones)):
                opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
            print()
            return opcion
        except ValueError:
            opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
        

def menu_Cliente():
    print('''Menú Cliente:
1. Hacer reserva 
2. Ir al buffet
3. Usar el minibar
4. Ver reservas activas 
5. Volver\n''')

def menu_Administrador(): 
    print('''Menú Administrador:
1. Dar empleado de alta
2. Dar empleado de baja
3. Asignar tareas
4. Control de ingreso y egreso
5. Inventario del Personal: Administrativo, Mantenimiento y Limpieza
6. Recaudación diaria
7. Volver\n''')
    
def menu_Personal_Administrativo():
    print('''Menú Administrativo:
1. Historial de reservas
2. Nomina de clientes del hotel
3. Elaborar informe estadístico
4. Visualización de las tareas pendientes
5. Realizar tarea pendiente
6. Volver\n''')
    
def menu_Mant_Limp(): 
    print('''Menú Empleados:
1. Visualización de las tareas pendientes
2. Realizar tarea pendiente
3. Volver\n''')