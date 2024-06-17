print ("Necesito tu nombre, edad y donde vives")

nombre = str (input("Cual es tu nombre: "))
edad = int (input("Cual es tu Edad: "))
Ciudad = str (input("De que ciudad eres: "))

if edad >= 18:
    print (" Estimado", nombre, "Podemos ver que eres mayor de edad y que vives en ", Ciudad)
elif edad >= 14:
    print ("Eres menor de edad y vives en ", Ciudad)
elif edad < 5:
      print ("Como puedes usar un pc?")