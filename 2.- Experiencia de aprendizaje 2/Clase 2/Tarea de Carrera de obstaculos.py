print ("Bienvenidos a la carrera de obstaculos")
print ("Comienza la carrera!!!")

Valla = str (input("Ves una valla? si / no: ")) 

#Valido si encontro una valla

if Valla == ("si"):
    print("     Entonces debes saltar la valla!!")
elif Valla == ("no"):
    print("     Continua corriendo!!")

Tunel = str (input("Ves un Tunel? si / no: "))

# Valido si encontro un tunel

if Tunel == "si":
    print("     Entonces atraviesa el tunel!")
elif Tunel == "no":
    print ("    Continua corriendo")

Laguna = str (input("ves una Laguna? si / no: "))

# Valido si encontro la laguna

if Laguna == "si":
    print ("    Debes nadar en la laguna")
    print ("    Lamentable perdiste la carrera al agotarte pero diste lo mejor de ti")
elif Laguna == "no":
    print ("    Felicitaciones por haber ganado")

 # En el apartado del input el programa siempre lo tomara como 
 # un STR aun que no tengas el str puesto