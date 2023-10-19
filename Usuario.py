class Usuario():
    def __init__(self, nombre: str, apellido: str, edad: int, sexo: str,dni: int, mail, contrasena):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
        self.dni=dni
        self.mail=mail
        self.contrasena=contrasena


        pass
    #verificar dni 
    #verificar sexo
    #verificar edad
    #verificar contrasena
    #aca no me esta verificando que tenga una longitud min
    def contrasena_fuerte(self):
        
        def contiene_numero(self):
            verifica = False
            for elemento in self.contrasena:
                if (ord(elemento) >= 48 and ord(elemento) <= 58):
                    verifica = True
            return verifica  
        
        def contiene_dos_mayusculas(self):
            contador = 0
            for elemento in self.contrasena:
                if (ord(elemento) >= 65 and ord(elemento) <= 90):
                    contador += 1
            
            if (contador >= 2):
                return True
            else:
                return False
            
        return contiene_numero(self) and contiene_dos_mayusculas(self)

    pass

class Cliente(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail, contrasena:str, saldo ):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.saldo=saldo
        

    pass

class Adminitrador(Usuario):
      def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)

    
    
    
class Empleado(Usuario):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str, legajo:int):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena)
        self.legajo = legajo
    def registro_ingreso(self):
        pass
    def registro_egreso(self):
        pass

class Limpieza(Empleado):
        def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str, legajo:int):
            super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena, legajo)
       
    
class Mantenimiento(Empleado):
     def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str, legajo:int):
         super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena, legajo)

class Limpieza(Empleado):
    def __init__(self,nombre: str, apellido: str, edad: int, sexo: str, dni: int, mail:str, contrasena: str, legajo:int):
        super().__init__(nombre, apellido, edad, sexo, dni, mail, contrasena, legajo)


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