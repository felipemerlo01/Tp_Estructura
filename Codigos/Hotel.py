from Cliente import Cliente
from Empleado import Empleado
from Funciones_extra import verificar_fecha_de_nacimiento, validar_fecha, verificar_dni, verificar_sexo, verificar_mail, verificar_contrasena
from datetime import datetime, date
import csv
from random import sample, randint

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = {}
        self.habitaciones = {}
        self.reservas = []
        
    def crear_usuario(self, opcion):
        nombre = input('Ingrese su nombre: ').capitalize()
        print()
        
        apellido = input('Ingrese su apellido: ').capitalize()
        print()

        fecha_de_nacimiento = verificar_fecha_de_nacimiento(validar_fecha(input("Ingrese su fecha de nacimiento (dd/mm/YYYY): ")))
        
        sexo = verificar_sexo(input("Ingrese su sexo (F/M): ").upper())
        
        dni = verificar_dni(input("Ingrese su DNI: "))
        
        mail = self.verificar_mail_existente(verificar_mail(input("Ingrese su mail: ")))
        
        contrasena = verificar_contrasena(input("Ingrese una contraseña. Debe contener al menos 8 caracteres, con un mínimo de 2 mayúsculas y 2 numeros: "))
        
        if (opcion == '1'):
            nuevo_usuario = Cliente(nombre, apellido, fecha_de_nacimiento, sexo, int(dni), mail, contrasena)
            self.usuarios[nuevo_usuario.mail] = nuevo_usuario
        
        elif (opcion == '2'):
            rol = self.verificar_rol(input("Ingrese su rol: ").capitalize())
            legajo = self.crear_legajo()
            
            nuevo_usuario = Empleado(nombre, apellido, fecha_de_nacimiento, sexo, int(dni), mail, contrasena, int(legajo), rol)
            self.usuarios[nuevo_usuario.mail] = nuevo_usuario
        
        print(f'\nSe ha creado el usuario de {nuevo_usuario.nombre} {nuevo_usuario.apellido} correctamente\n')
        return nuevo_usuario
        
    # verificar si el mail ya existe
    def verificar_mail_existente(self, mail: str):
        while (mail in self.usuarios): 
            mail = self.verificar_mail(input('Mail ya existente. Ingrese otro mail: '))
        print()
        return mail
    
    # verificar rol 
    def verificar_rol(self, rol: str):
        while rol not in ("Administrativo", "Mantenimiento", "Limpieza"):
            rol = input("Rol invalido. Ingrese un rol valido: ")
        print()
        return rol

    # Buscar al ultimo usuario que tiene legajo y al nuevo usuario agregarle el siguiente legajo 
    def crear_legajo(self): 
        for usuario in reversed(self.usuarios.values()):
            if hasattr(usuario, 'legajo'):
                nuevo_legajo = int(usuario.legajo) + 1
                return nuevo_legajo
            
    # valido el mail y contrasena al iniciar sesión
    def validar_inicio_sesion(self, mail: str, contrasena: str): 
        while (True):
            if (mail not in self.usuarios):
                mail = verificar_mail(input('Mail no encontrado. Ingrese un mail registrado: '))
            elif (hasattr(self.usuarios[mail], 'estado') and self.usuarios[mail].estado == 'Inactivo'):
                mail = verificar_mail(input('Usuario inactivo. Ingrese el mail de un usuario activo: '))
            else:
                while (contrasena != self.usuarios[mail].contrasena):
                    contrasena = input('Contraseña incorrecta. Ingrese nuevamente: ')
                print()
                return self.usuarios[mail]
            contrasena = input('Ingrese su contraseña: ')
    
    # Iniciar sesion
    def iniciar_sesion(self):
        mail = verificar_mail(input('Ingrese su mail: '))
        contrasena = input('Ingrese su contraseña: ')
        
        return self.validar_inicio_sesion(mail, contrasena)
    
    # Buscar un empleado en la base por su legajo, si no lo encuentra no se lo vuelve a pedir
    def buscar_empleado(self, legajo):
        for usuario in self.usuarios.values():
            if hasattr(usuario, 'legajo'):  
                if (usuario.legajo == legajo):
                    return usuario
        return
    
    # Calcular porcentaje de ocupacion del hotel
    def procentaje_de_ocupacion(self):
        # Antes que nada, hay que actualizar el atributo ocupada de las habitaciones
        self.actualizar_estado_habitaciones()
        
        # Ahora, ya si hago lo otro
        capacidad_total = len(self.habitaciones)
        capacidad_ocupada = 0
        for habitacion in self.habitaciones.values():
            if habitacion.ocupada == True:
                capacidad_ocupada += 1
        porcentaje_ocupacion=round((capacidad_ocupada/capacidad_total)*100,2)
        return porcentaje_ocupacion

    # Calcular porcentaje de ocupacion del hotel por tipo de habitacion ("Simple", "Doble", "Familiar", "Suite")
    def procentaje_de_ocupacion_por_tipo_de_habitación(self):
        # Antes que nada, hay que actualizar el atributo ocupada de las habitaciones
        self.actualizar_estado_habitaciones()
        
        # Ahora, ya si hago lo otro
        tipos = ("Simple", "Doble", "Familiar", "Suite")
        procentaje_ocupacion_por_tipo=[]
        for tipo in tipos:
            capacidad_parcial = 0
            ocupacion_del_tipo = 0
            for habitacion in self.habitaciones.values():
                if habitacion.tipo == tipo:
                    capacidad_parcial += 1
                    if habitacion.ocupada == True:
                        ocupacion_del_tipo += 1
            procentaje_ocupacion_del_tipo = round((ocupacion_del_tipo/capacidad_parcial)*100,2)
            procentaje_ocupacion_por_tipo.append(procentaje_ocupacion_del_tipo)
        return procentaje_ocupacion_por_tipo
    
    # Calculo de recaudacion diaria del hotel
    def recaudacion_diaria(self):
        ingreso_del_dia = 0
        hoy = datetime.now()
        for reserva in self.reservas:
            check_out_dt = datetime.strptime(reserva.check_out, '%d/%m/%Y')
            if (check_out_dt == hoy):
                ingreso_del_dia += (reserva.gastos_ocupacion + reserva.gastos_buffet + reserva.gastos_minibar)
        return ingreso_del_dia

    def cantidad_de_clientes_por_tipo(self):
        self.actualizar_estado_habitaciones()
        topes_de_categoria = {'1':250000,'2':600000}
        Cant_clientes_por_cat = [0,0,0]
        hoy = datetime.now()
        for reserva in self.reservas:
            check_out_dt = datetime.strptime(reserva.check_out, '%d/%m/%Y')
            if (reserva.habitacion.ocupada == True and check_out_dt >= hoy):
                gastos = reserva.gastos_ocupacion + reserva.gastos_buffet + reserva.gastos_minibar
                if gastos <= topes_de_categoria['1']:
                    Cant_clientes_por_cat[0]+=1
                elif topes_de_categoria['1'] < gastos <= topes_de_categoria['2']:
                    Cant_clientes_por_cat[1]+=1
                elif topes_de_categoria['2'] < gastos:
                    Cant_clientes_por_cat[2]+=1
                        
        return topes_de_categoria,Cant_clientes_por_cat
        
    def crear_informe_estadistico(self):
        fecha = date.today()
        procentaje_ocupacion = self.procentaje_de_ocupacion() 
        porcentajes_parciales_de_ocupacion = self.procentaje_de_ocupacion_por_tipo_de_habitación()
        ganancia_del_dia = self.recaudacion_diaria()
        cantidad_de_clientes_por_tipo = self.cantidad_de_clientes_por_tipo()

        with open('Informe_estadistico.txt','w') as informe:
            informe.write(f"\t\t\t\tInforme estadistico del Hotel \n\n Fecha: \t{fecha}\n\n\n\n")
            informe.write(f"Porcentaje de ocupacion general: \t{procentaje_ocupacion}% \n\n")
            informe.write(f"Porcentajes De ocupacion por tipo de habitacion: \n")
            informe.write(f"\t\tSimple: {porcentajes_parciales_de_ocupacion[0]}% \n")
            informe.write(f"\t\tDoble: {porcentajes_parciales_de_ocupacion[1]}% \n")
            informe.write(f"\t\tFamiliar: {porcentajes_parciales_de_ocupacion[2]}% \n")
            informe.write(f"\t\tSuite: {porcentajes_parciales_de_ocupacion[3]}% \n\n\n")
            informe.write(f"Ganancia del dia: {ganancia_del_dia} \n\n")
            informe.write(f"Cantidad de Clientes actuales, clasificados por nivel de inversion:\n")
            informe.write(f"\t\t Clase 1 (inversion menor a {cantidad_de_clientes_por_tipo[0]['1']}): {cantidad_de_clientes_por_tipo[1][0]} \n")
            informe.write(f"\t\t Clase 2 (inversion entre {cantidad_de_clientes_por_tipo[0]['1']} y {cantidad_de_clientes_por_tipo[0]['2']}): {cantidad_de_clientes_por_tipo[1][1]} \n")
            informe.write(f"\t\t Clase 3 (inversion mayor a {cantidad_de_clientes_por_tipo[0]['2']}): {cantidad_de_clientes_por_tipo[1][2]} \n")
        
        print(f'Se creó el informe estadistico correctamente a las {datetime.strftime(datetime.now(),"%H:%M")}\n')
    
    def actualizar_estado_habitaciones(self):
        for habitacion in self.habitaciones.values():
            habitacion.actualizar_estado_ocupacion(self.reservas)

    def generar_ingreso_y_egreso_aleatorio(self):
        empleados = []
        for usuario in self.usuarios.values():
            if (hasattr(usuario, 'legajo') and usuario.legajo != 1 and usuario.estado == 'Activo'): #Es empleado
                empleados.append(usuario)
        
        empleados_presentes = sample(empleados, randint(3,15))
        
        for empleado in empleados_presentes:
            empleado.registro_ingreso()
            empleado.registro_egreso()
        
        return empleados_presentes
        

######################### ACTUALIZACION DE BASES DE DATOS

    # Actualizar todas las bases
    def actualizar_bases_de_datos(self, path):
        try:
            self.actualizar_base_reservas(path + 'db_Reservas.csv')
            self.actualizar_base_usuarios(path + 'db_Usuarios.csv')
            print('Se guardo la información correctamente')
        except Exception as e:
            print('Ha habido un error en el guardado.')
            print(f"Error al escribir en el archivo CSV: {e}")
            
    # Metodo actualizar base usuarios
    def actualizar_base_usuarios(self, path):
        columnas = ('Nombre','Apellido','Fecha de nacimiento','Sexo','DNI','Mail','Contrasenia','Legajo','Rol','Estado','Tareas')
        with open(path, 'w', newline='',encoding='utf-8') as csv_usuarios:
            csv_writer = csv.writer(csv_usuarios)
            csv_writer.writerow(columnas)           
            
            for usuario in self.usuarios.values():
                if (isinstance(usuario, Cliente)):
                    fila = (usuario.nombre, usuario.apellido, usuario.fecha_de_nacimiento, usuario.sexo, str(usuario.dni), usuario.mail, usuario.contrasena, '', 'Cliente', '', '')
                elif (isinstance(usuario, Empleado)):
                    if not usuario.tareas.empty():
                        tareas_string = ', '.join(map(str, list(usuario.tareas.queue)))
                    else:
                        tareas_string = ""

                    fila = (usuario.nombre, usuario.apellido, usuario.fecha_de_nacimiento, usuario.sexo, str(usuario.dni), usuario.mail, usuario.contrasena, str(usuario.legajo), usuario.rol, usuario.estado, tareas_string)
                else:
                    fila = (usuario.nombre, usuario.apellido, usuario.fecha_de_nacimiento, usuario.sexo, str(usuario.dni), usuario.mail, usuario.contrasena, str(usuario.legajo), 'admin', '', '')
                csv_writer.writerow(fila)
        
    # Metodo actualizar base reservas
    def actualizar_base_reservas(self, path):
        columnas = ('Mail','Numero de habitacion','Check-in','Check-out','Fecha reserva','Gastos buffet','Gastos minibar')
        with open(path, 'w', newline='') as csv_reservas:
            csv_writer = csv.writer(csv_reservas)
            csv_writer.writerow(columnas)

            for reserva in self.reservas:
                fila = (reserva.mail_usuario, reserva.num_hab, reserva.check_in, reserva.check_out, reserva.fecha_reserva, str(reserva.gastos_buffet), str(reserva.gastos_minibar))
                csv_writer.writerow(fila)
    

    