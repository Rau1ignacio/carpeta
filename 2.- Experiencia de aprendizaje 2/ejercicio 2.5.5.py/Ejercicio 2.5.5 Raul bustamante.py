# Codigo 2.5.5
# Raul Bustamante Gonzalez

# Usuarios con valor inicial vacio
# None es Vacio

Usuario1 = None
Usuario2 = None
Usuario3 = None
Contrasena1 = None
Contrasena2 = None
Contrasena3 = None

'''
Dentro del siguiente while tengo
Menu = Este es el principal donde se Registra e inicia sesion
Menu2 = Este es para eligir el usuario con cual iniciar sesion
Menu3 = Este es para hacer llamadas y enviar correo electronico
'''

while True:

    #Primer menu
    Menu = int (input("""\n Primero debes registrar usuario/s y despues iniciar sesion
                      
        1.- Iniciar sesion
        2.- Registrar usuario
        3.- Salir

    Opcion: """))

    if Menu == 1:
        
        # Iniciar sesion
        # Validacion de usuarios

        print ("\n Haz selecionado INICIAR SESION\n")

        # Puse un segundo menu para eligir con cual usuario iniciar sesion
        Menu2 = int (input('''\n Con que usuario quieres iniciar sesion
                           
        1.- Usuario 1
        2.- Usuario 2
        3.- Usuario 3
        4.- Salir
                           
        Opcion: '''))

        if Menu2 == 1:

            ValidacionUsuario1 = (input("Inicia sesion usuario 1: "))
            ValidacionContraseña1 = int (input("Ingrese contraseña usuario 1: "))

            if ValidacionUsuario1 == Usuario1 and ValidacionContraseña1 == Contraseña1:

                print ("\nUsuario 1: correcto")
                print ("Contraseña 1: correcto\n")

                while True:

                    Menu3 = int (input(''' 
                                       
                    1) Realizar llamada
                    2) Enviar correo electrónico
                    3) Cerrar sesión

                    Opcion: '''))
                    while True:

                        if Menu3 == 1:

                            # Donde la opción 1 debe solicitar un número de celular,
                            # éste deberá comenzar con 9 y su tamaño es de 9 dígitos (ejemplo: 985447561).
                            # el Try es corroborar que ponga numeros
                            try:
                                NumeroDeCelular1 = int(input('''\nIngrese tu número de celular.
                                Debe comenzar con 9 y tener 9 dígitos (ejemplo: 985447561): '''))
                            except ValueError:
                                print("\nError: Debes ingresar números enteros. Inténtalo de nuevo.\n")
                                continue

                            # Convertir el número de celular a cadena para calcular la longitud
                            CantidadDenumeros1 = len(str(NumeroDeCelular1))

                            if CantidadDenumeros1 != 9:
                                print("\nDebes ingresar un número de 9 dígitos.\n")
                                continue

                            # Validar que el número de celular comience con 9
                            if str(NumeroDeCelular1).startswith("9"):
                                print("\nExcelente, ahora debes ir a la sección de enviar un correo electrónico.\n")
                                break
                            else:
                                print("\nEl número de celular debe comenzar con 9. Inténtalo de nuevo.\n")
                                continue

                        elif Menu3 == 2:

                        # La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un 
                        # carácter de “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
                            CorreoElectronico1 = input("Por favor, ingresa tu correo electrónico: ")
                        # Bucle for
                            for char in CorreoElectronico1:

                                if char == '@':

                                    print("\n Correo electrónico válido. \n")
                                    Mensaje1 = (input("\n Envia el mensaje del correo electronico \n Mensaje: "))
                                    print ("\n Este mensaje se envio: ",Mensaje1,"\n")
                                    break

                                else:
                                    print("El correo electrónico debe contener al menos un carácter '@'.")
                
                        else:
                            # Para salir del menu y bucle.
                            print ("Salir")
                            break

            else:
                print ("    \nUsuario o contraseña incorrecto o no registrado!!!!!!\n")
                print ("    Vuelva a ingresar\n")

        elif Menu2 == 2:

            ValidacionUsuario2 = (input("Inicia sesion usuario 2: "))
            ValidacionContraseña2 = int (input("Ingrese contraseña usuario 2: "))

            if ValidacionUsuario2 == Usuario2 and ValidacionContraseña2 == Contraseña2:

                print ("\nUsuario 2 correcto")
                print ("Contraseña 2 correcto\n")

                Menu3 = int (input('''
                1) Realizar llamada
                2) Enviar correo electrónico
                3) Cerrar sesión

                Opcion: '''))

                if Menu3 == 1:

                    # Donde la opción 1 debe solicitar un número de celular,
                    # éste deberá comenzar con 9 y su tamaño es de 9 dígitos (ejemplo: 985447561).
                    # el Try es corroborar que ponga numeros
                    try:
                        NumeroDeCelular2 = int(input('''\nIngrese tu número de celular.
                        Debe comenzar con 9 y tener 9 dígitos (ejemplo: 985447561): '''))
                    except ValueError:
                        print("\nError: Debes ingresar números enteros. Inténtalo de nuevo.\n")
                        continue

                    # Convertir el número de celular a cadena para calcular la longitud
                    CantidadDenumeros2 = len(str(NumeroDeCelular2))

                    if CantidadDenumeros2 != 9:
                        print("\nDebes ingresar un número de 9 dígitos.\n")
                        continue

                    # Validar que el número de celular comience con 9
                    if str(NumeroDeCelular2).startswith("9"):
                        print("\nExcelente, ahora debes ir a la sección de enviar un correo electrónico.\n")
                        break
                    else:
                        print("\nEl número de celular debe comenzar con 9. Inténtalo de nuevo.\n")
                        continue

                elif Menu3 == 2:

                    # La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un 
                    # carácter de “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
                    CorreoElectronico2 = input("Por favor, ingresa tu correo electrónico: ")
                        # Bucle for
                    for char in CorreoElectronico2:

                        if char == '@':

                            print("\n Correo electrónico válido. \n")
                            Mensaje2 = (input("\n Envia el mensaje del correo electronico \n Mensaje: "))
                            print ("\n Este mensaje se envio: ",Mensaje2,"\n")
                            break

                    else:
                        print("El correo electrónico debe contener al menos un carácter '@'.")
                
                else:
                        # Para salir del menu y bucle.
                        print ("Salir")
                        break

            else:
                print ("    \nUsuario o contraseña incorrecto o no registrado!!!!!!\n")
                print ("    Vuelva a ingresar\n")

        elif Menu2 == 3:


            ValidacionUsuario3 = (input("Inicia sesion usuario 3: "))
            ValidacionContraseña3 = int (input("Ingrese contraseña usuario 3: "))

            if ValidacionUsuario3 == Usuario3 and ValidacionContraseña3 == Contraseña3:

                print ("\nUsuario 3 correcto")
                print ("Contraseña 3 correcto\n")

                Menu3 = int (input('''
                1) Realizar llamada
                2) Enviar correo electrónico
                3) Cerrar sesión

                Opcion: '''))

                if Menu3 == 1:

                    # Donde la opción 1 debe solicitar un número de celular,
                    # éste deberá comenzar con 9 y su tamaño es de 9 dígitos (ejemplo: 985447561).
                    # el Try es corroborar que ponga numeros
                    try:
                        NumeroDeCelular3 = int(input('''\nIngrese tu número de celular.
                        Debe comenzar con 9 y tener 9 dígitos (ejemplo: 985447561): '''))
                    except ValueError:
                        print("\nError: Debes ingresar números enteros. Inténtalo de nuevo.\n")
                        continue

                    # Convertir el número de celular a cadena para calcular la longitud
                    CantidadDenumeros3 = len(str(NumeroDeCelular3))

                    if CantidadDenumeros3 != 9:
                        print("\nDebes ingresar un número de 9 dígitos.\n")
                        continue

                    # Validar que el número de celular comience con 9
                    if str(NumeroDeCelular3).startswith("9"):
                        print("\nExcelente, ahora debes ir a la sección de enviar un correo electrónico.\n")
                        break
                    else:
                        print("\nEl número de celular debe comenzar con 9. Inténtalo de nuevo.\n")
                        continue

                elif Menu3 == 2:

                    # La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un 
                    # carácter de “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
                    CorreoElectronico3 = input("Por favor, ingresa tu correo electrónico: ")
                        # Bucle for
                    for char in CorreoElectronico3:

                        if char == '@':

                            print("\n Correo electrónico válido. \n")
                            Mensaje3 = (input("\n Envia el mensaje del correo electronico \n Mensaje: "))
                            print ("\n Este mensaje se envio: ",Mensaje3,"\n")
                            break

                    else:
                        print("El correo electrónico debe contener al menos un carácter '@'.")
                
                else:
                        # Para salir del menu y bucle.
                        print ("Salir")
                        break

            else:
                print ("    \nUsuario o contraseña incorrecto o no registrado!!!!!!\n")
                print ("    Vuelva a ingresar\n")

        elif Menu2 == 4:
            # Para salir del menu y bucle.
            print ("Salir")
            break

        else:
            print ("    \nUsuario o contraseña incorrecto!!!!!!\n")
            print ("    Vuelva a ingresar\n")

    elif Menu == 2:

        # pongo el usuario 1

        Validacion1 = (input("\n Quieres agregar un usuario 1 - si / no: "))
        Validacion1 = Validacion1.lower()

        if Validacion1 == "si":
            # Valido usuario 1
            print ("    \nExcelente\n")
            print ("\nResgistrar usuario 1")
            Usuario1 = (input("\n Añada nuevo nombre de usuario 1: "))
            Contraseña1 = int (input("\n Escriba nueva contraseña 1: "))
            print ("\nTu usuario 1 es:", Usuario1, "\nTu contraseña 1 es: ", Contraseña1)
            print ("Ahora puedes volver al menu principal o agregar otro usuario")

            Validacion2 = (input("\n Quieres agregar un usuario 2 - si / no: "))
            Validacion2 = Validacion2.lower()

            if Validacion2 == "si":
                # Pongo y Valido el usuario 2
                print ("    \nExcelente\n")
                print ("\nResgistrar usuario 2")
                Usuario2 = (input("\n Añada nuevo nombre de usuario 2: "))
                Contraseña2 = int (input("\n Escriba nueva contraseña 2: "))
                print ("\nTu usuario 2 es:", Usuario2, "\nTu contraseña 2 es: ", Contraseña2)
                print ("Ahora puedes volver al menu principal o agregar otro usuario")

                Validacion3 = (input("\n Quieres agregar un usuario 3 - si / no: "))
                Validacion3 = Validacion3.lower()

                if Validacion3 == "si":
                    # Pongo y Valido el usuario 3
                    print ("    \nExcelente\n")
                    print ("\nResgistrar usuario 3")
                    Usuario3 = (input("\n Añada nuevo nombre de usuario 3: "))
                    Contraseña3 = int (input("\n Escriba nueva contraseña 3: "))
                    print ("\nTu usuario 3 es:", Usuario3, "\nTu contraseña 3 es: ", Contraseña3,"\n")
                    print (" Ahora vuelve al menu princial para iniciar sesion")

                elif Validacion3 == "no":
                    print ("\n De vuelta al menu principal")

            elif Validacion2 == "no":
                    print ("\n De vuelta al menu principal")

        elif Validacion1 == "no":
                    print ("\n De vuelta al menu principal")

        else:
            print ("\n Vuelva a ingresar!!")

    elif Menu == 3:

        # Para salir del menu y bucle.
        print ("\nSalir\n")
        break