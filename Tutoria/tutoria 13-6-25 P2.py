

capitales = {
    'Chile': 'Santiago',
    'Peru': 'Lima',
    'Ecuador': 'Quito'
}

#recorrer por clave(key)
print('#recorrer por clave(key)\n')

for pais in capitales:
    print('la capital de', pais, 'es', capitales[pais])

#recorrer por valor(VALUES)
print('\n------------------')

print('\n#recorrer por valor(VALUES)\n')

for capital in capitales.values():

    print(capital, 'es una linda ciudad\n')

# Recorrer por el par clave: valor (items)
print('------------------\n')
for p,c in  capitales.items():
    print(c, 'es la capital de:', p)