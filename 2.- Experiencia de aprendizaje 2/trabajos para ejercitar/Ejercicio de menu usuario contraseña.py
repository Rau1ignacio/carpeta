Total = 0

 #Debo PONER MAAS TRY para corroborar la informacion puesta en el codigo

while True:

    Menu = int (input("""
        1.- Registrar usuario
        2.- Iniciar suma
        3.- Salir
    Opcion: """))

    if Menu == 1:

        print ("\nResgristrar usuario")
        Usuario1 = (input("\n Añada nuevo nombre de usuario: "))
        Contraseña1 = int (input("\n Escriba nueva contraseña: "))
        print ("\nTu usuario es:", Usuario1, "\nTu contraseña es: ", Contraseña1)
        Validacion = (input("\n si / no: "))

        if Validacion == "si":
            print ("    \nExcelente\n")
        else:
            print ("Vuelva a ingresar")

    elif Menu == 2:
        print ("\n Haz selecionado INICIAR SUMA\n")
        print ("Iniciar Sesionn")
        ValidacionUsuario = (input("Inicia sesion: "))
        ValidacionContraseña = int (input("Ingrese contraseña: "))

        if ValidacionUsuario == Usuario1 and ValidacionContraseña == Contraseña1:

            print ("\nUsuario correcto")
            print ("Contraseña correcto\n")

            print ("Ahora pon numeros para sumar\n")

            Suma1 = int (input("Ingrese suma 1: "))
            suma2 = int (input("Ingresa suma 2: "))

            Total = Suma1 + suma2

            print ("    \nEl total de la suma es: ",Total,"\n")
            #print (" Quieres volver al menu?")
            #Aqui podemos poner que vulva al menu para sali o que siga sumando
            
        else:
            print ("    \nUsuario o contraseña incorrecto!!!!!!\n")
            print ("    Vuelva a ingresar\n")
            
    elif Menu == 3:
        print ("Salir")
        break