#Actividad de ciclo de desiciones
# Esta incompleto!!

Pasajes = int (input(" Cuantos pasajes deseas vender?: "))

TotalIngresos = 0

for i in range(Pasajes):
    TotalIngresos = int (input(" 1- Cual es el valor de cada pasaje?: \n 2- Break (Para valores no numericos)"))
    Total = print("tu total es de:", TotalIngresos * Pasajes)
    TotalIngresos = str("Has seleccionado un valor no numerico")