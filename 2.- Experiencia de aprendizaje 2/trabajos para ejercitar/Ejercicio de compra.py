print("\n Menu de verduleria \n")



PAPAS3kg = 2000
NARANJA1kg = 1000
Limon = 1000

Total = 0


while True:

    Menu = int (input('''
1.- Comprar
2.- Pagar
3.- Salir

    Opcion: '''))

    if Menu == 1:

        Menucompra = str (input('''
    Menu de compras:
                                
        3 kilos de PAPAS  = 2000 
        1 kilo de NARANJA = 1000
        1 LIMON           = 1000
                        
    Opcion: '''))
        
        if Menucompra.lower == "papas":
            print ("\nHas seleccionado comprar Papas")
            Total = PAPAS3kg + Total
            print (" llevas $",Total)
            if meni

