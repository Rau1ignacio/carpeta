

nombre = input("Ingrese su nombre ")

n1 = float(input('ingrese nota 1: '))
n2 = float(input('ingrese nota 2: '))
n3 = float(input('ingrese nota 3: '))

# Validar nota (1 y 7)

if 1<=n1<=7 and 1<=n2<=7 and 1<=n3<=7:

    p1 = n1*0.25
    p2 = n2*0.35
    p3 = n3*0.40
    
    promedio = p1 + p2 + p3
    
    # El round es para aproximar el promedio round(promedio, 1) ese , 1 es el valor decimal que vamos aproximar
    
    print(  nombre , 'Tu promedio es: ', round(promedio,1))

    if promedio >= 3.95:
        print ('    Genial aprovaste')
    else:
        print ('    Has reprobado')

else:
    print ('notas(s) fuera de rango!!')