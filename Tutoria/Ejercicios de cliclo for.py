print ("Bienbenidos al 1er ejercicio de ciclo for")

print ('''
 Ingresar por teclado 5 números enteros, luego debe indicar:
 Cuántos números son mayores a cero
 Cuántos números son menores a cero
 Cuántos números son iguales a cero
 ''')


# Ingresar 5 números enteros por teclado
numeros = []
for i in range(5):
    num = int(input("Ingrese un número entero: "))
    numeros.append(num)

# Contar cuántos números son mayores a cero, menores a cero y iguales a cero
mayores_cero = 0
menores_cero = 0
iguales_cero = 0

for num in numeros:
    if num > 0:
        mayores_cero += 1
    elif num < 0:
        menores_cero += 1
    else:
        iguales_cero += 1

# Mostrar los resultados
print("Cantidad de números mayores a cero:", mayores_cero)
print("Cantidad de números menores a cero:", menores_cero)
print("Cantidad de números iguales a cero:", iguales_cero)
