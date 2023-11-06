from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre: str, apellido: str, fecha_de_nacimiento: str, sexo: str, dni: int, mail: str, contrasena: str, legajo: int):
        super().__init__(nombre, apellido, fecha_de_nacimiento, sexo, dni, mail, contrasena)
        self.legajo = legajo           

    def dar_empleado_de_alta(self, hotel):
        empleado = hotel.crear_usuario('2')
        hotel.usuarios[empleado.mail] = empleado
        print(f"{empleado.nombre} {empleado.apellido} ha sido dado de alta como empleado.")
    
    def dar_empleado_de_baja(self, hotel):
        nombre = input("Nombre del empleado: ").capitalize()
        apellido = input("Apellido del empleado: ").capitalize()
        
        empleado = hotel.buscar_empleado(nombre, apellido)
            
        if (empleado != None):
            empleado.estado = "Inactivo" # Cambiar el estado del empleado a "Inactivo"
            print(f"{empleado.nombre} {empleado.apellido} ha sido dado de baja como empleado.")
        else:
            print(f'{nombre} {apellido} no es un usuario en el sistema.')
        
    def asignar_empleado_menos_ocupado(self, usuarios, rol):
        lista_empleados_de_interes = []
        for usuario in usuarios.values():
            if (hasattr(usuario, 'rol') and usuario.rol == rol):
                lista_empleados_de_interes.append(usuario)
                
        trabajador_menos_ocupado = min(lista_empleados_de_interes, key=lambda trabajador: trabajador.tareas.qsize())
        return trabajador_menos_ocupado
    
    def asignar_tareas(self, hotel):
        nombre = input("Nombre del empleado: ").capitalize()
        apellido = input("Apellido del empleado: ").capitalize()
        
        empleado = hotel.buscar_empleado(nombre, apellido)
        
        # NOTA CAMILO: yo decia que asigne y escriba lo que le pinte en el input
        # osea no valida nada, tipo si el empleado es de manteimiento le podes poner 'hola' o 'limpiar' qcy
        # REVISAR si es que quieren complejizarla mas segun el rol del empleado o si solo puede asignar ciertas tareas en particular y no cualquier input
        
        tarea = input('Ingrese la tarea a asignar: ')
        
        if (empleado != None):
            empleado.tareas.put(tarea)
            print (f"La tarea fue asignada al empleado/a {empleado.nombre} {empleado.apellido} correctamente")
        else:
            print(f'{nombre} {apellido} no es un usuario en el sistema.')      
        
    # METODO BUSCAR HISTORIAL DE RESERVAS, NO ENTIENDO SI ES PEDIR UN CLIENTE Y MOSTRAR LAS DE ÉL O VER TODAS LAS RESERVAS DEL HOTEL? O PODRIAMOS DAR LAS 2 OPCIONES?
    
    # METODO NOMINA DE CLIENTES DEL HOTEL, NO ENTIENDO SI ES CLIENTES HOSPEDADOS ACTUALMENTE O CLIENTES REGISTRADOS COMO CLIENTES
    
    