total = 0

while True:
    
    # El jugador 1 ingresa el numero de 5 digitos 

    num_j1 = input("ingresa el numero de 5 digitos : ")

    #se valida si el numero cumple con el largo correspondiente utilizando la funcion len para contar el dato ingresado
    
    if len(num_j1) != 5 :
    
        print("el numero ingresado debe tener 5 digitos ")
    
    else:
     
        #comienza la comprobacion del digito ingresado por el jugador 1 
        
        print("Comienza el juego -- --")

        #Se recorre el numero ingresado donde cada numero que va avanzando se guarda en la variable i 
    
        for i in range(len(num_j1)):
    
            #Se le pide al usuario que ingrese el digito adivinar
    
            digito_j2= input(f"ingrese el digito N° {i+1} adivinar ")

            #En cada iteracion o vuelta que da comprobará  el valor ingresado por el usuario , en este caso ira comprobando en orden desde el primer digito hasta el ultimo
            #Si el digito ingresado en la iteracion corresponde , este le dara felicitacion al usuario que adivino un numero 
    
            if digito_j2 == num_j1[i]:
    
                print(f"Felicidades Adivinaste el digito correctamente en la posicion {i+1}  ")
                total = total + 1 

            else :
    
                #en caso el numero ingresado no coincida con la compribacion le avisara al usuario que no es correcto y pasara a la siguiente iteracion 
        
                print("intentalo de nuevo ")

        #si el jugador a sumado 5 puntos por cada acierto este le avisara que gano y que adivino el numero incognito         
    
        if total == 5 :
    
            print(f"Felicidades adivinaste los todos los numeros , el numero adivinar es {num_j1}")
            break
    
        #si no cumple con los puntos , este le avisa que perdio y le da el numero que no pudo adivinar y empezando de nuevo 
    
        else:
            print(f"Lo siento intentalo de nuevo el numero a adivinar era {num_j1} ")
                
