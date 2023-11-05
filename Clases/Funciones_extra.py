from datetime import datetime
from re import fullmatch
import pandas as pd
from Cliente import Cliente
from Empleado import Empleado
from Administrador import Administrador
from Habitacion import Habitacion
from Reserva import Reserva

# Funcion de validar fechas para uso general (no me parece que vaya como metodo de la clase): --> convendria ponerlo en un archivo de validaciones sueltas, poner ahi tambien las de hotel
# "Las funciones de validaciones generales pueden estar en un archivo aparte, el cuál se importará
# cuando fuera necesario."

def validar_fecha(fecha_ingresada):
    while (True):
        try:
            datetime.strptime(fecha_ingresada, "%d/%m/%Y")
            return fecha_ingresada
        except ValueError:
            fecha_ingresada = input('Ingrese un formato de fecha valido (dd/mm/YYYY): ')
            
def validar_fecha_posteriori(fecha_antes, fecha_despues):
    while (True):
        fecha_ant = datetime.strptime(fecha_antes, '%d/%m/%Y')
        fecha_des = datetime.strptime(fecha_despues, '%d/%m/%Y')

        if (fecha_des > fecha_ant):
            return fecha_despues
        else:
            fecha_despues = validar_fecha(input('Incorrecto. Ingrese una fecha posterior: '))
            
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
    while (True):
        try:
            while (int(dni) > 99999999 or int(dni) < 10000000):
                dni = input('Ingrese un DNI valido: ')
            return dni
        except ValueError:
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

def validar_si_no(opcion):
    while (opcion not in ['Si', 'No']):
        opcion = input('Ingrese una opción valida (Si/No): ').capitalize()
    return opcion

def validar_precio(precio):
    while (True):
        try:
            while (int(precio) < 1):
                precio = input('Ingrese un precio máximo valido: ')
            return precio
        except ValueError:
            precio = input('Ingrese un precio máximo valido: ')
    
def validar_capacidad_min(capacidad):
    while (True):
        try:
            while (int(capacidad) < 1  or int(capacidad) > 4):
                dni = input('Ingrese una de las capacidades disponibles: ')
            return capacidad
        except ValueError:
            capacidad = input('Ingrese una capacidad válida: ')
            
#########################

# Funciones de lectura de las bases de datos: 

# Lee la base de datos CSV de usuarios y crea los objetos usuarios, los agrega al diccionario de Hotel y le agrega las reservas existente a los respectivos clientes, asi como tareas a empleados
def leer_Usuarios(path, Hotel):
    usuarios = pd.read_csv(path)
    
    for _, row in usuarios.iterrows():
        if (row["Rol"] == "Cliente"):
            nuevo_usuario = Cliente(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"])
            Hotel.usuarios[nuevo_usuario.mail] = nuevo_usuario
            for reserva in Hotel.reservas:
                if (reserva.mail == nuevo_usuario.mail):
                    nuevo_usuario.reservas.append(reserva)
        elif (row["Rol"] in ["Mantenimiento", "Administrativo", "Limpieza"]):
            nuevo_empleado = Empleado(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"], int(row["Legajo"]), row["Rol"])
            Hotel.usuarios[nuevo_empleado.mail] = nuevo_empleado
            tasks = row['Tareas'].split(', ')
            for task in tasks:
                nuevo_empleado.tareas.put(task)
            
        elif (row["Rol"] == "Administrador"):
            administrador = Administrador(row["Nombre"], row["Apellido"], row["Fecha de nacimiento"], row["Sexo"], int(row["DNI"]), row["Mail"], row["Contrasenia"])
            Hotel.usuarios[administrador.mail] = administrador
    
    
# Lee la base de datos CSV de habitaciones y las agrega al hotel
def leer_Habitaciones(path, Hotel):
    habitaciones = pd.read_csv(path)
    
    for _, row in habitaciones.iterrows():
        nueva_habitacion = Habitacion(int(row["Numero"]), int(row["Precio por noche"]), int(row["Capacidad"]), row["Tipo"], row["Banio privado"], row["Balcon"], row['Ocupada'])
        Hotel.habitaciones[nueva_habitacion.numero] = nueva_habitacion

# Lee la base de datos CSV de reservas y las agrega al hotel
def leer_Reservas(path, Hotel):
    reservas = pd.read_csv(path)

    for _, row in reservas.iterrows():
        nueva_reserva = Reserva(row["mail"], row["numero_hab"], row["Fecha_inicio"], row["Fecha_fin"], row['Fecha_reserva'])
        Hotel.reservas.append(nueva_reserva)
        
#######################

def menu_principal():
    print('''Bienvenido al menu:
1. Iniciar sesión
2. Registrar usuario
3. Salir''')
    
def menu_registro():
    print('''
1. Registrarse como cliente
2. Registrarse como empleado
3. Volver''')
    
def validar_opcion_menu(opcion, cantidad_opciones):
    while (True):
        try:
            while (not (1 <= int(opcion) <= cantidad_opciones)):
                opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
            return opcion
        except ValueError:
            opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
        

def menu_Cliente():
    print('''
1. Hacer reserva 
2. Ir al buffet
3. Usar el minibar
4. Ver gastos  
5. Volver''')

def menu_Administrador(): 
    print('''
1. Dar empleado de alta
2. Dar empleado de baja
3. Asignar tareas
4. Control de ingreso y egreso
5. Inventario del Personal: Administrativo, Mantenimiento y Limpieza
6. Recaudación diaria
7. Volver''')
    
def menu_Personal_Administrativo():
    print('''
1. Historial de sus reservas
2. Nomina de clientes del hotel
3. Informes estadísticos
4. Volver''')
    
def menu_Informe_estadístico(): 
    print('''
1. Porcentaje de ocupación del hotel
2. Porcentaje de ocupacion de acuerdo al tipo de habitación
3. Cantidad de clientes por tipo
4. Volver''')
    
def menu_Mant_Limp(): 
    print('''
1. Registro ingreso
2. Registro egreso
3. Visualización de las tareas activas
4. Realizar tarea pendiente
5. Volver''')