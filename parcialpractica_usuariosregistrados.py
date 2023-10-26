    
# def validar_usuario(usuarioingresado, contraseñaingresada, base_usuarios):
#     usuario_encontrado = False
#     contraseña_encontrada = False
    
#     for usuario in base_usuarios:
#         if (usuario.email == usuarioingresado):
#             usuario_encontrado = True
            
#     if (usuario_encontrado == True):
#         for usuario in base_usuarios:
#             if (usuario.contraseña == contraseñaingresada):
#                 contraseña_encontrada = True
    
#     return usuario_encontrado,contraseña_encontrada

# Clase

import numpy as np
from typing import Union

class UsuarioRegistrado:
    def __init__(self, nombre: str, apellido: str, dni: int, email: str, contraseña: str):
        self.nombre = nombre
        if (any(elemento.isdigit() for elemento in self.nombre)):
            raise ValueError('El nombre no debe contener numeros')
        self.apellido = apellido
        if (any(elemento.isdigit() for elemento in self.apellido)):
            raise ValueError('El apellido no debe contener numeros')
        self.dni = dni
        if (any(elemento.isalpha() for elemento in str(self.dni)) and len(str(self.dni)) != 8):
            raise ValueError('El DNI no debe contener letras')
        
        self.email = email
        self.contraseña = contraseña
        if (self.contraseña == '' or self.contraseña.isspace()):
            raise ValueError('La contraseña no puede estar vacia')

    def cambiar_contraseña(self, contraseña_nueva):
        if (contraseña_nueva == '' or contraseña_nueva.isspace()):
            raise ValueError('La nueva contraseña no puede estar vacia')

        self.contraseña = contraseña_nueva  #--> Validacion en el menu

class UsuarioInvitado:
    def __init__(self, nombre: str, apellido: str, dni: int, email: str):
        self.nombre = nombre
        if (any(elemento.isdigit() for elemento in self.nombre)):
            raise ValueError('El nombre no debe contener numeros')
        self.apellido = apellido
        if (any(elemento.isdigit() for elemento in self.apellido)):
            raise ValueError('El apellido no debe contener numeros')
        self.dni = dni
        if (any(elemento.isalpha() for elemento in str(self.dni)) and len(str(self.dni)) != 8):
            raise ValueError('El DNI no debe contener letras')
        self.email = email
        self.cantidadvecesingresa = 0 
        
    def cambiar_nombre(self, nombre_nuevo):
        if (any(elemento.isdigit() for elemento in nombre_nuevo)):
            raise ValueError('El nombre no debe contener numeros')
        self.nombre = nombre_nuevo
        
    def cambiar_apellido(self, apellido_nuevo):
        if (any(elemento.isdigit() for elemento in apellido_nuevo)):
            raise ValueError('El nombre no debe contener numeros')
        self.apellido = apellido_nuevo
    
    def cambiar_email(self, email_nuevo):
        self.email = email_nuevo
        
    def cambiar_dni(self, dni_nuevo):
        if (any(elemento.isalpha() for elemento in dni_nuevo) or len(str(dni_nuevo)) != 8):
            raise ValueError('El DNI no debe contener letras')
        self.dni = dni_nuevo

class SistemaDeInformacion:
    def __init__(self, usuariosInvitados, usuariosRegistrados):
        self.usuariosRegistrados = usuariosRegistrados
        self.usuariosInvitados = usuariosInvitados
    
    def registrar_usuarios(self, usuario: Union[UsuarioInvitado, UsuarioRegistrado]):
        if isinstance(usuario, UsuarioInvitado):
            self.usuariosInvitados.append(usuario)
        if isinstance(usuario, UsuarioRegistrado):
            self.usuariosRegistrados.append(usuario)
            
    def menu(self):
        # Funciones    
        def mostrar_menu():
            print('''Bienvenido al menu:
        1.   Ingresar como registrado
        2.   Ingresar como invitado
        3.   Crear usuario
        4.   Salir
        ''')

        def submenu_registrado():
            print('''¿Que datos desea actualizar?
        1.   Cambiar contraseña
        2.   Volver
        ''')

        def submenu_invitado():
            print('''¿Que datos desea actulizar?
        1.   Nombre
        2.   Apellido
        3.   DNI
        4.   Email
        5.   Volver
        ''') 
            
        # def validar_usuario(usuarioingresado, variableingresada, variable, base_usuarios):
        #     usuario_encontrado = False
        #     variable_encontrada = False
            
        #     for usuario in base_usuarios:
        #         if (usuario.email == usuarioingresado):
        #             usuario_encontrado = True
                    
        #     if (usuario_encontrado == True):
        #         for usuario in base_usuarios:
        #             if (usuario.variable == variableingresada):
        #                 variable_encontrada = True
            
        #     return usuario_encontrado,variable_encontrada
        
        def validar_usuario(usuarioingresado, variableingresada, variable, base_usuarios):
            variable_encontrada = False

            for usuario in base_usuarios:
                if usuario.email == usuarioingresado:
                    if getattr(usuario, variable) == variableingresada:
                        variable_encontrada = True

            return variable_encontrada

        continuar = True
        while (continuar == True):
            mostrar_menu()
            opcion = int(input("¿Que opción desea elegir?"))                      
            if (opcion == 1):
                usuarioingresado = input("Ingrese su mail: ")
                contraseñaingresada = input("Ingrese su contraseña: ")
                contraseña_encontrada = validar_usuario(usuarioingresado,contraseñaingresada, 'contraseña', self.usuariosRegistrados)
                
                if (contraseña_encontrada): 
                    indice = None
                    for i, usuario in enumerate(self.usuariosRegistrados):
                        if usuario.email == usuarioingresado:
                            indice = i
                            break
                
                if (contraseña_encontrada == True):
                    submenu_registrado()
                    
                    volver = False
                    while (volver == False):
                        sub_opcion = int(input("Ingrese la opcion: "))
                        if (sub_opcion == 1):             
                            nueva_contraseña = input(f'Hola {self.usuariosRegistrados[indice].nombre}, ingrese la nueva contraseña: ')
                            self.usuariosRegistrados[indice].cambiar_contraseña(nueva_contraseña)
                            print('Se cambio correctamente')
                            volver = True
                        else:
                            volver = True
                else:
                    print("Los datos ingresados son incorrectos")
            if (opcion == 2):
                usuarioingresado = input("Ingrese su mail: ")
                DNIingresado = int(input('Ingrese su DNI: '))
                dni_encontrado = validar_usuario(usuarioingresado,DNIingresado,"dni",self.usuariosInvitados)
                
                
                if dni_encontrado == True:
                    indice = None
                    for i, usuario in enumerate(self.usuariosInvitados):
                        if usuario.email == usuarioingresado:
                            indice = i
                            break
                
                    self.usuariosInvitados[indice].cantidadvecesingresa += 1
                
                if dni_encontrado == True:
                    submenu_invitado()

                    volver = False
                    while (volver == False):
                        sub_opcion = int(input("Ingrese la opcion: "))
                        if (sub_opcion == 1):   #Nombre          
                            nuevo_nombre = input(f'Hola {self.usuariosInvitados[indice].nombre}, ingrese su nuevo nombre: ')
                            self.usuariosInvitados[indice].cambiar_nombre(nuevo_nombre) 
                            print('Se cambio correctamente')   
                        elif (sub_opcion == 2):  #Apellido
                            nuevo_apellido = input(f'Hola {self.usuariosInvitados[indice].nombre}, ingrese su nuevo apellido: ')
                            self.usuariosInvitados[indice].cambiar_apellido(nuevo_apellido)
                            print('Se cambio correctamente')    
                        elif (sub_opcion == 3):  #DNI
                            nuevo_dni = input(f'Hola {self.usuariosInvitados[indice].nombre}, ingrese su nuevo dni: ')
                            self.usuariosInvitados[indice].cambiar_dni(nuevo_dni)
                            print('Se cambio correctamente') 
                        elif (sub_opcion == 4):  #Email
                            nuevo_email = input(f'Hola {self.usuariosInvitados[indice].nombre}, ingrese su nuevo email: ')
                            
                            if (any(usuario.email == nuevo_email for usuario in self.usuariosInvitados) or any(usuario.email == nuevo_email for usuario in self.usuariosRegistrados)):
                                raise ValueError("Ese mail ya esta asociado a una cuenta")
                            
                            self.usuariosInvitados[indice].cambiar_email(nuevo_email)
                            print('Se cambio correctamente')
                        else:
                            volver = True
                    
                if (opcion == 3):
                    pass    
                
                else:
                    print("Los datos ingresados son incorrectos")
            if (opcion == 3):
                continuar = False

usuario1 = UsuarioRegistrado("Juan", "Pérez", 12345678, "juanperez@gmail.com", "clave123")
usuario2 = UsuarioRegistrado("Ana", "López", 98765432, "analopez@yahoo.com", "abcxyz")
usuario3 = UsuarioRegistrado("Carlos", "Gómez", 55555555, "carlosgomez@hotmail.com", "password123")
usuario4 = UsuarioRegistrado("María", "Rodríguez", 77777777, "maria@gmail.com", "miclave")
usuario5 = UsuarioRegistrado("Estefano", "Hoguero", 11111111, "juanquiro@gmail.com", "contraseña")
usuario6 = UsuarioRegistrado("Laura", "García", 22222222, "laura@hotmail.com", "clave12345")
usuario7 = UsuarioRegistrado("Pedro", "Sánchez", 33333333, "pedro@yahoo.com", "qwerty")
usuario8 = UsuarioRegistrado("Elena", "Martínez", 44444444, "elena@gmail.com", "miclave123")
usuario9 = UsuarioRegistrado("Alejandro", "Fernández", 66666666, "alejandro@gmail.com", "password123")
usuario10 = UsuarioRegistrado("Sofía", "González", 88888888, "sofia@yahoo.com", "abcxyz123")
usuario11 = UsuarioRegistrado("Andrés", "López", 99999999, "andres@gmail.com", "clave456")
usuario12 = UsuarioRegistrado("Luis", "Ramírez", 12121212, "luis@yahoo.com", "mipassword")
usuario13 = UsuarioRegistrado("Patricia", "Díaz", 34343434, "patricia@hotmail.com", "123456")
usuario14 = UsuarioRegistrado("Carmen", "Soto", 56565656, "carmen@gmail.com", "contraseña123")
usuario15 = UsuarioRegistrado("Javier", "Gutiérrez", 78787878, "javier@yahoo.com", "qwerty123")
usuario16 = UsuarioRegistrado("Isabel", "Torres", 99998888, "isabel@gmail.com", "miclave789")
usuario17 = UsuarioRegistrado("Antonio", "Gómez", 55556666, "antonio@yahoo.com", "abcdef")
usuario18 = UsuarioRegistrado("Silvia", "Luna", 77774444, "silvia@gmail.com", "password456")
usuario19 = UsuarioRegistrado("Diego", "Pérez", 11113333, "diego@hotmail.com", "clave789")
usuario20 = UsuarioRegistrado("Natalia", "Sánchez", 22227777, "natalia@gmail.com", "mipassword123")
usuario21 = UsuarioRegistrado("Juan","Quiro",66658889,"juanquiro@gmail.com","contraseña")
usuario22 = UsuarioRegistrado("Pablo","Portio",22222222,"pabloportio@gmail.com","banana")
usuario23 = UsuarioRegistrado("Lucia","Menendez",33333333,"luciamenendez@gmail.com","agua")
usuario24 = UsuarioRegistrado("Yamila","Caseres",44444444,"yamilacaseres@gmail.com","carne")
usuario25 = UsuarioRegistrado("Estefano","Hoguero",11111111,"juanquiro@gmail.com","contraseña")

invitado1 = UsuarioInvitado("Pedro", "Forca", 23458765, "forquita@hotmail.com")
invitado2 = UsuarioInvitado("Laura", "Gómez", 87654321, "laura@gmail.com")
invitado3 = UsuarioInvitado("Juan", "Martínez", 54321678, "juanm@yahoo.com")
invitado4 = UsuarioInvitado("Ana", "Pérez", 12345678, "ana@hotmail.com")
invitado5 = UsuarioInvitado("Sofía", "López", 98765432, "sofialopez@gmail.com")
invitado6 = UsuarioInvitado("Diego", "Ramírez", 34567890, "diego@yahoo.com")
invitado7 = UsuarioInvitado("María", "Gutiérrez", 56789012, "maria@gmail.com")
invitado8 = UsuarioInvitado("Carlos", "Díaz", 78901234, "carlosd@hotmail.com")
invitado9 = UsuarioInvitado("Elena", "Soto", 43210987, "elena@yahoo.com")
invitado10 = UsuarioInvitado("Javier", "Torres", 21098765, "javi@gmail.com")
invitado11 = UsuarioInvitado("Isabel", "Gómez", 65432109, "isabelg@hotmail.com")
invitado12 = UsuarioInvitado("Antonio", "Luna", 98765432, "antonio@yahoo.com")
invitado13 = UsuarioInvitado("Patricia", "Fernández", 10987654, "patricia@gmail.com")
invitado14 = UsuarioInvitado("Luis", "Hernández", 43210987, "luis@hotmail.com")
invitado15 = UsuarioInvitado("Natalia", "Martín", 87654321, "natalia@yahoo.com")
invitado16 = UsuarioInvitado("Carmen", "García", 98765432, "carmen@gmail.com")
invitado17 = UsuarioInvitado("Andrés", "Pérez", 10987654, "andres@hotmail.com")
invitado18 = UsuarioInvitado("Silvia", "Ramírez", 65432109, "silvia@yahoo.com")
invitado19 = UsuarioInvitado("Alejandro", "Gómez", 43210987, "alejandro@gmail.com")
invitado20 = UsuarioInvitado("Cecilia", "Sánchez", 87654321, "cecilia@hotmail.com")

array_de_usuarios_invitados = np.array([invitado1, invitado2, invitado3, invitado4, invitado5, 
                                        invitado6, invitado7, invitado8, invitado9, invitado10, 
                                        invitado11, invitado12, invitado13, invitado14, invitado15, 
                                        invitado16, invitado17, invitado18, invitado19, invitado20])

array_de_usuarios_registrados = np.array([usuario1, usuario2, usuario3, usuario4, usuario5,
                                          usuario6, usuario7, usuario8, usuario9, usuario10,
                                          usuario11, usuario12, usuario13, usuario14, usuario15,
                                          usuario16, usuario17, usuario18, usuario19, usuario20,
                                          usuario21, usuario22, usuario23, usuario24, usuario25])

# Después de crear los usuarios, agrégalos al sistema
sistema = SistemaDeInformacion(array_de_usuarios_invitados, array_de_usuarios_registrados)

sistema.menu()

""" sistema = SistemaDeInformacion()

# Datos de usuarios registrados
usuarios_registrados_data = [
    ("Juan", "Pérez", 12345678, "juanperez@gmail.com", "clave123"),
    ("Ana", "López", 98765432, "analopez@yahoo.com", "abcxyz"),
    ("Carlos", "Gómez", 55555555, "carlosgomez@hotmail.com", "password123"),
    ("María", "Rodríguez", 77777777, "maria@gmail.com", "miclave"),
    ("Estefano", "Hoguero", 11111111, "juanquiro@gmail.com", "contraseña"),
    ("Laura", "García", 22222222, "laura@hotmail.com", "clave12345"),
    ("Pedro", "Sánchez", 33333333, "pedro@yahoo.com", "qwerty"),
    ("Elena", "Martínez", 44444444, "elena@gmail.com", "miclave123"),
    ("Alejandro", "Fernández", 66666666, "alejandro@gmail.com", "password123"),
    ("Sofía", "González", 88888888, "sofia@yahoo.com", "abcxyz123"),
    ("Andrés", "López", 99999999, "andres@gmail.com", "clave456"),
    ("Luis", "Ramírez", 12121212, "luis@yahoo.com", "mipassword"),
    ("Patricia", "Díaz", 34343434, "patricia@hotmail.com", "123456"),
    ("Carmen", "Soto", 56565656, "carmen@gmail.com", "contraseña123"),
    ("Javier", "Gutiérrez", 78787878, "javier@yahoo.com", "qwerty123"),
    ("Isabel", "Torres", 99998888, "isabel@gmail.com", "miclave789"),
    ("Antonio", "Gómez", 55556666, "antonio@yahoo.com", "abcdef"),
    ("Silvia", "Luna", 77774444, "silvia@gmail.com", "password456"),
    ("Diego", "Pérez", 11113333, "diego@hotmail.com", "clave789"),
    ("Natalia", "Sánchez", 22227777, "natalia@gmail.com", "mipassword123"),
    ("Juan", "Quiro", 66658889, "juanquiro@gmail.com", "contraseña"),
    ("Pablo", "Portio", 22222222, "pabloportio@gmail.com", "banana"),
    ("Lucía", "Menéndez", 33333333, "luciamenendez@gmail.com", "agua"),
    ("Yamila", "Caseres", 44444444, "yamilacaseres@gmail.com", "carne"),
    ("Estefano", "Hoguero", 11111111, "juanquiro@gmail.com", "contraseña")
]

# Crear y agregar usuarios registrados al sistema
for data in usuarios_registrados_data:
    usuario = UsuarioRegistrado(*data)
    sistema.registrar_usuarios(usuario)

# Datos de usuarios invitados
usuarios_invitados_data = [
    ("Pedro", "Forca", 23458765, "forquita@hotmail.com"),
    ("Laura", "Gómez", 87654321, "laura@gmail.com"),
    ("Juan", "Martínez", 54321678, "juanm@yahoo.com"),
    ("Ana", "Pérez", 12345678, "ana@hotmail.com"),
    ("Sofía", "López", 98765432, "sofialopez@gmail.com"),
    ("Diego", "Ramírez", 34567890, "diego@yahoo.com"),
    ("María", "Gutiérrez", 56789012, "maria@gmail.com"),
    ("Carlos", "Díaz", 78901234, "carlosd@hotmail.com"),
    ("Elena", "Soto", 43210987, "elena@yahoo.com"),
    ("Javier", "Torres", 21098765, "javi@gmail.com"),
    ("Isabel", "Gómez", 65432109, "isabelg@hotmail.com"),
    ("Antonio", "Luna", 98765432, "antonio@yahoo.com"),
    ("Patricia", "Fernández", 10987654, "patricia@gmail.com"),
    ("Luis", "Hernández", 43210987, "luis@hotmail.com"),
    ("Natalia", "Martín", 87654321, "natalia@yahoo.com"),
    ("Carmen", "García", 98765432, "carmen@gmail.com"),
    ("Andrés", "Pérez", 10987654, "andres@hotmail.com"),
    ("Silvia", "Ramírez", 65432109, "silvia@yahoo.com"),
    ("Alejandro", "Gómez", 43210987, "alejandro@gmail.com"),
    ("Cecilia", "Sánchez", 87654321, "cecilia@hotmail.com")
]

# Crear y agregar usuarios invitados al sistema
for data in usuarios_invitados_data:
    invitado = UsuarioInvitado(*data)
    sistema.registrar_usuarios(invitado)
 """


# Continúa agregando los demás usuarios invitados

# Ahora los usuarios estarán en el sistema y podrás utilizarlos según sea necesario



# # Funciones    
# def menu():
#     print('''Bienvenido al menu:
# 1.   Ingresar como registrado
# 2.   Ingresar como invitado
# 3.   Crear usuario
# 4.   Salir
# ''')

# def submenu_registrado():
#     print('''¿Que datos desea actualizar?
# 1.   Cambiar contraseña
# 2.   Salir
# ''')

# def submenu_invitado():
#     print('''¿Que datos desea actulizar?
# 1.   Nombre
# 2.   Apellido
# 3.   DNI
# 4.   Email
# 5.   Volver
# ''') 
    
# def validar_usuario(usuarioingresado, variable, base_usuarios):
#     usuario_encontrado = False
#     variable_encontrada = False
    
#     for usuario in base_usuarios:
#         if (usuario.email == usuarioingresado):
#             usuario_encontrado = True
            
#     if (usuario_encontrado == True):
#         for usuario in base_usuarios:
#             if (usuario.variable == variable):
#                 variable_encontrada = True
    
#     return usuario_encontrado,variable_encontrada

# continuar = True
# while (continuar == True):
#     menu()
#     opcion = input("¿Que opción desea elegir?")
#     base_usuarios = []
#     if opcion == 1:
#         submenu_registrado()
#         nueva_opcion = input("Ingrese la opcion: ")

#         if nueva_opcion == 1:
#             usuarioingresado = input("Ingrese su mail: ")
#             contraseñaingresada = input("Ingrese su contraseña: ")
            
#             usuario_encontrado,contraseña_encontrada = validar_usuario(usuarioingresado,contraseñaingresada,self.)
            
#             if (contraseña_encontrada == True):
#                 indice =  np.where(base_usuarios.mail == usuarioingresado) #--> Busca el indice en el array cuando coincide 
#                 nueva_contraseña = input(f'Hola {base_usuarios[indice].nombre}, ingrese la nueva contraseña: ')
#                 base_usuarios[indice].cambiar_contraseña(nueva_contraseña)
#             else:
#                 print("Los datos ingresados son incorrectos")

#     if opcion == 2:
#         usuarioingresado = input("Ingrese su mail: ")
#         DNIingresado = int(input('Ingrese su DNI: '))
        
#         usuario_encontrado,contraseña_encontrada = validar_usuario(usuarioingresado,contraseñaingresada,base_usuarios)

#     if opcion == 3:
#         continuar = False


# """"""