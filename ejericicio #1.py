# Haz un programa en Python que pida por teclado al usuario su nombre, su edad y su
# altura en metros.
import math

nombre = input("¿Como te llamas? \n")
edad = input("¿Cuantos años tienes? \n")
altura = float(input("¿Cuanto mides? \n"))
centimetros, metros = math.modf(altura)
centimetros *= 100
centimetros = int(centimetros)
metros = int(metros)

print(f"El usuario {nombre} tiene {edad} años y mide {metros} metro y {centimetros} centimetros")