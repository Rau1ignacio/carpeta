

opciones = ("1.- Opcion 1", "2.- opcion 2", "3.- opcion 3", "4.- Salir")

while True:
    print ("Seleccione una opcion: ")

    for opcion in opciones:
        print(opcion)

    try:
        seleccion = int (input("Ingrese el numero de la opcion: "))

        if seleccion == 1:
            print("Ha selecionado la opcion 1.")
        elif seleccion == 2:
            print("Ha selecionado la opcion 2.")
        elif seleccion == 3:
            print("Ha selecionado la opcion 3.")
        elif seleccion == 4:
            print("Saliendo del programa...")
            break
        else: (" opcion o valida. porfavor, seleccione una opcion")

    except ValueError:
        print (" Entrada no valida. por favor, ingrese un numero")

'''
menu_principal = ["Opción 1", "Opción 2", "Opción 3"]

while True:
    print("Seleccione una opción:")
    for i, opcion in enumerate(menu_principal, 1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            opcion_principal = int(input("Ingrese el número de opción: "))
            if 1 <= opcion_principal <= len(menu_principal):
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    if opcion_principal == 1:
        print("Seleccionaste la Opción 1.")
        # Aquí puedes agregar la lógica para la Opción 1

    elif opcion_principal == 2:
        print("Seleccionaste la Opción 2.")
        # Aquí puedes agregar la lógica para la Opción 2

    elif opcion_principal == 3:
        print("Seleccionaste la Opción 3.")
        # Aquí puedes agregar la lógica para la Opción 3

    else:
        print("Opción inválida.")

    while True:
        continuar = input("¿Deseas volver al menú principal? (S/N): ")
        if continuar.upper() == 'S' or continuar.upper() == 'N':
            break
        else:
            print("Entrada inválida. Por favor, ingrese 'S' o 'N'.")

    if continuar.upper() != 'S':
        break
'''
         