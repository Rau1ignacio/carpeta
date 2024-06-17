print("Bienvenidos a la estacion de usuario")

nivelBencina = int (input("Cuantos litros de bencina tiene su auto?: "))

# Verifico si e nivel de bencina es mayor a 10 o menor a 10 para cargar o no cargar bencina

if nivelBencina <= 10:
    print ("    Le sugiero cargar mas bencina")
    TipodeBencina = int (input("    Elige el tipo de bencina que deseas cargar 93-95-97: "))
else:
    if nivelBencina >= 10:
        print ("    no es necesario cargar bencina")

# Validar el tipo de bencina

if TipodeBencina == 93:
    print ("    Se esta cargando Bencina regular")
else:
    if TipodeBencina == 95:
        print ("    Se esta cargando bencina plus")
    else:
        if TipodeBencina == 97:
            print ("    Se esta cargando bencina premium")
        else:
          # En este caso no puse ningun valos como != o <> porque me dejaba un error que no podia solucionarlo
          # Pero al dejarlo sin valor me quedo bueno el codigo
          if TipodeBencina:
               print ("         Su opcion no es valida")
               print ("             Vuelve hacer el proceso")
            
