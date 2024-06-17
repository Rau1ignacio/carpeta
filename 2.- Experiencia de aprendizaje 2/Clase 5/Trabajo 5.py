cantidad_pasajes = int (input ("ingrese la cantidades pasajes a vender: "))

totalingreso = 0


while cantidad_pasajes != 0 :


    try:

        for cantidad in range (cantidad_pasajes):

            valor = int ( input (f"ingrese el valor del pasaje numero  {cantidad}  : " ))
            totalingreso = totalingreso + valor

            if cantidad + 1 == cantidad_pasajes:

                print(f" \n El total a pagar es ${totalingreso} \n" )
                cantidad_pasajes = 0

                break

    except ValueError:

        print(f"El total a pagar es {totalingreso} ")
        break