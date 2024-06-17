
try:

    numero = int( input("ingrese un numero: "))

    for i in range (numero):

        print (f"se va a repetir {i}")

except ValueError:

    print ("algo salio mal -> Vuelva a ingresar un numero ")
