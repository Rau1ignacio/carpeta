'''
Obtener la nmenor cantidad entre tres
numero ingresados
'''

n1 = int (input("Ingrese nº1: "))
n2 = int (input("Ingrese nº2: "))
n3 = int (input("Ingrese nº3: "))

if n1<n2 and n1<n3:
    print("numero 1 es el menor de todos")

elif n2<n1 and n2<n3:
    print(" numero 2 es el menor de todos")
    
else:
    print (" numero 3 es menor de todos")