# Juego sobre desifrar claves numericas Experiencia 1

print ("\nBienvenidos al juego de adivinar los 5 digitos\n")
print ("    El juego consta de 2 jugadores")
print ("    El jugador 1ro pone los digito que debera adivinar el jugaror 2")

print (" \n Jugador 1, Pone los 5 digitos que tienen que ser el 0 al 9: \n")

#jugador 1 pone en orden los digitos y se guarda cada uno en una variable

digito1 = int (input("  Pon el PRIMER  numero que debe adivinar: "))
digito2 = int (input("  Pon el SEGUNDO numero que debe adivinar: "))
digito3 = int (input("  Pon el TERCER  numero que debe adivinar: "))
digito4 = int (input("  Pon el CUARTO  numero que debe adivinar: "))
digito5 = int (input("  Pon el QUINTO  numero que debe adivinar: "))

print("\nAhora es tu turno jugador 2, debes ir adivinando los digitos de la clave\n")

intentos = 6

#Comienzo de bucle para adivinar

while True:

    # Aqui se ponen los digitos del jugador 2 y con sus respectivos intentos que le quedan en caso de que falle
    # En el caso que se equivoque en un digito tendra que volver a empezar en el digito 1

    in1 = int (input("Adivina el digito 1: "))

    if in1 == digito1:

        print("     \n Has adivinado el digito 1:", digito1 ,"_ _ _ _\n")

        int2 = int (input("Adivina el digito 2: "))

        if int2 == digito2:

            print("     \n Has adivinado el digito 2: ", digito1 , digito2," _ _ _\n")

            int3 = int (input("Adivina el digito 3: "))

            if int3 == digito3:

                print("     \n Has adivinado el digito 3: ", digito1 , digito2, digito3," _ _\n")

                int4 = int (input("Adivina el digito 4: "))

                if int4 == digito4:
                  
                    print("     \n Has adivinado el digito 4: ", digito1 , digito2, digito3, digito4," _\n")

                    int5 = int (input("Adivina el digito 5: "))

                    if int5 == digito5:
                  
                        print ("     \n Has adivinado el digito 5: ", digito1 , digito2, digito3, digito4, digito5, "\n")
                        print ("\n FELICIDADES HAS ADIVINADO TODOS LOS DIGITOS\n")
                        Jugar = (input("Quieres jugar otra vez? si / no :"))

                        if Jugar == "si":
                            print ("Volvamos a jugar!!")
                        else:
                            print ("\n Fin del juego \n")
                        break
                  
                    else:
                        print("\nNo has adivinado, vuelve a intentarlo\n")
                        intentos = intentos -1
                        print("Te quedan:", intentos, "intentos.")
                else:
                    print("\nNo has adivinado, vuelve a intentarlo\n")
                    intentos = intentos -1
                    print("Te quedan:", intentos, "intentos.")
            else:
                print("\nNo has adivinado, vuelve a intentarlo\n")
                intentos = intentos -1
                print("Te quedan:", intentos, "intentos.")
        else:
            print("\nNo has adivinado, vuelve a intentarlo\n")
            intentos = intentos -1
            print("Te quedan:", intentos, "intentos.")
    else:
        print("\nNo has adivinado, vuelve a intentarlo\n")
        intentos = intentos -1
        print("Te quedan:", intentos, "intentos.")  
        
    if intentos == 0:
        print("\n SE TE ACABARON LOS INTENTOS \n    El numero secreto era: ",digito1, digito2, digito3, digito4,digito5)
        break

    