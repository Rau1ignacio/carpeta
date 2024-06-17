nombre = ""

while True:
        

    # los Try deben ir siempre donde el usuario debe validar informacion ingresada    
    try:
        print ("1 ingresar a menu 1")
        print ("2")
        print ("3")    

        resp = input("ingresa una opcion: ")

        while resp == "1":
            print ("1 Entrar si su nombre es juan")
            print ("2 cambiar nombre")
            print ("3 Volver al menu 1")    

            resp2 = input("ingresa una opcion: ")


            if resp2 == "3":
                break
            if resp2 == "2":

                nombre = input("cual es el nombre: ")

                #len para contar carateres y el .strip es para eliminar los espacios

                len(nombre.strip())


            elif resp2 == "1" and nombre == "juan":
                print (f"ingresaste de manera correcta {nombre}")

    except:
        print ("error")



# Apuntes

    # Siempre que nos pidan repetir debe ir un for.
    # El "len(variable)" nos permite contar caracteres
    # El .strip() es para eliminar los espacios
    # EL len y strip quizas nos lo pidan para la prueba