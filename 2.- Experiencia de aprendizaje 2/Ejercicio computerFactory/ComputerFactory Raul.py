
DiscosDuros = 10
MemoriasRam = 3
PlacasMadre = 10
FuentesDePoder = 0

Ususario = None
ContraseñaUsuario = None
Ususario_inicio = None
ContraseñaUsuario_inicio = None

while True:

    print("\nElige la opcion")
    Menu = int (input("""

    1.- Iniciar Sesión
    2.- Salir

    Opcion: """))

# Bloque 1
        
    if Menu == 1:

        Menu2 = int (input("""

        1.- Rol de ADMIN
        2.- Rol de comprador

        Opcion: """))
# Bloque 2
        if Menu2 == 1:
            
            while True: 
                MenuADMIN = int (input("""
                Menu admin
                                        
                1.- Dar de Alta usuario
                2.- Abastecer Local
                3.- Sacar Reporte
                4.- Cerrar Sesión

                Opcion: """))
    # Bloque 2.1
                if MenuADMIN == 1:

                    '''Esta opción permitirá crear un usuario con el Rol
                    comprador el cual el cual podrá iniciar sesión'''

                    print ("Debes crear un nuevo 'usuario comprador'")
                    Ususario = (input("Nombre: "))
                    ContraseñaUsuario = int (input("Contraseña en numeros: "))

                    print (f"""
    El usuario ingresado es: {Ususario} 
    La contraseña ingresada es: {ContraseñaUsuario}""")
                    # Aqui vuelve al a Menu Admin

                if MenuADMIN == 2:

                    '''Abastecer Local: 
                    1.- Preguntara cuantos productos querrá abastecer,
                    luego ira 
                    2.- preguntando por cada producto y cuantos elementos se desea
                    agregar, solo debe aceptar números como cantidad para aumentar ,
                    3.- estos valores deben ser actualizados al stock general'''

                    print (f"""
                    Estos son los productos en Stock:
                                        
                        1.- Discos duros      = {DiscosDuros}
                        2.- Memorias Ram      = {MemoriasRam}
                        3.- Placas madres     = {PlacasMadre}
                        4.- Fuentes de  poder = {FuentesDePoder}
                
                        """)
                    Cantidad_abastecer_DiscosDuros = int (input("¿Cuantas cantidades de discos duros quieres agregar?: "))
                    DiscosDuros = DiscosDuros + Cantidad_abastecer_DiscosDuros

                    Cantidad_abastecer_MemoriasRam = int (input("¿Cuantas cantidades de Memorias Ram quieres agregar?: "))
                    MemoriasRam = MemoriasRam + Cantidad_abastecer_MemoriasRam

                    Cantidad_abastecer_PlacasMadre = int (input("¿Cuantas cantidades de Placas Madres quieres agregar?: "))
                    PlacasMadre = PlacasMadre + Cantidad_abastecer_PlacasMadre

                    Cantidad_abastecer_FuentesDePoder = int (input("¿Cuantas cantidades de Fuendes de poder quieres agregar?: "))
                    FuentesDePoder = FuentesDePoder + Cantidad_abastecer_FuentesDePoder

                    print (f"""
                    Estos son los productos en Stock ACTUALIZADOS!:
                                        
                        1.- Discos duros      = {DiscosDuros}
                        2.- Memorias Ram      = {MemoriasRam}
                        3.- Placas madres     = {PlacasMadre}
                        4.- Fuentes de  poder = {FuentesDePoder}\n """)
                    
                    print ("**Volveras al menu Admin**")
                    
                elif MenuADMIN == 3:

                    '''Este modulo mostrara un total de los productos
                    existentes'''

                    print (f'''
    Reporte de Stock:
                        
        1.- Discos duros      = {DiscosDuros}
        2.- Memorias Ram      = {MemoriasRam}
        3.- Placas madres     = {PlacasMadre}
        4.- Fuentes de  poder = {FuentesDePoder}
        
    Si quieres actualizar el reporte debes ir a "2.- Abastecer local"''')
                    
                elif MenuADMIN == 4:

                    '''Este módulo devolverá al menú principal'''

                    print ("cerrando sesion")
                    break

        elif Menu2 == 2:
                
            print ("Iniciar sesion como comprador")
            Ususario_inicio = (input("Usuario: "))
            ContraseñaUsuario_inicio = int (input("Contraseña: "))

            if Ususario_inicio == Ususario and ContraseñaUsuario_inicio == ContraseñaUsuario:
                print ("\nFelicidades has iniciado sesion con exito")
                
                while True: 

                    MenuComprador = int (input("""

                    1.- Comprar Productos
                    2.- Pagar Cuenta
                    3.- Cerrar Sesión

                    Opcion: """))

                    if MenuComprador == 1:

                        '''al usuario se le mostrara una lista de productos
                        disponibles con sus valores :'''
                        DiscosDurosValor = 50000
                        MemoriasRamValor = 35000
                        PlacasMadreValor = 40000
                        FuentesDePoderValor = 40000

                        print ('''

                        1.- Discos Duros     $50.000
                        2.- Memorias Ram     $35.000
                        3.- Placas Madre     $40.000
                        4.- Fuentes de poder $40.000\n''')

                        Compra1 = int (input ("Cuantos discos duros quieres comprar: "))
                        Compra1 = Compra1 * DiscosDurosValor

                        Compra2 = int (input ("Cuantas Memorias Ram quieres comprar: "))
                        Compra2 = Compra2 * MemoriasRamValor


                        Compra3 = int (input ("Cuantas Placas madres quieres comprar: "))
                        Compra3 = Compra3 * PlacasMadreValor


                        Compra4 = int (input ("Cuantas Fuentes de poder quieres comprar: "))
                        Compra4 = Compra4 * FuentesDePoderValor
                        
                        Total = Compra1 + Compra2 + Compra3 + Compra4

                        print (f"""Total
                                
                        Discos duros: ${Compra1}
                        Memorias Ram: ${Compra2}
                        Placas Madre: ${Compra3}
                        Fuentes de poder: ${Compra4}
                        
                        Total a pagar: ${Total}""")
                        print ("\nDebes volver al menu para Pagar cuenta\n")
                        break

                    elif MenuComprador == 2:
                        print ("\nPagar cuentas\n")

                        print (f"Total a pagar: ${Total}")
                        Boton = int (input("\nPresiona 1 para pagar: "))
                        if Boton == 1:
                            print ("Compra finalizada")
                            break
                        else:
                            print ("Error")

                    elif MenuComprador == 3:
                        print ("cerrar sesion")
                    break

            else:
                print ("\nUsuario o contraseña incorrecto. Vuelve a intentar\n")
    elif Menu == 2:
        print ("Has selecionado salir")
        break
