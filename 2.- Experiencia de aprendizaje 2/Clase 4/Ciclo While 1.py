# ciclo WHILE

'''
a = 5

while(a>0):
    print (f"Elvalor de a es : {a}")
    a= int (input("ingrese un numero: "))
'''

# Este es un  ejemplo del Mientras de PSeint
# En este caso hacemos un menu con el ciclo While (Mientras)
# donde se repitira el ciclo hasta selecciona 3 - salir

op = 1

print("bienvenidos")

while op != 3:

  # el \n nos permite saltar de linea al mostrar el codigo

    print(" Opcion 1: comprar \n Opcion 2: Vender \n Opcion 3: salir")
    
    op = int(input("Escoja una opcion: "))