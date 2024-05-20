# Haz un programa de Python que pida un número entero N al usuario entre 10 y 20.
# Muestra por pantalla todos los números enteros entre el 1 y el N.
# Muestra por pantalla todos los números enteros entre el 30 y el N, en orden inverso.

n = int(input("Numero entre 10 y 20: "))

if n < 10 or n > 20:
    print("Ingresa un numero mayor a 10 y menor a 20")
    n = int(input("Numero entre 10 y 20: "))

print("Cuenta progresiva")
for i in range(1, n + 1):
    print(i)

print("\nCuenta regresiva")
for i in range(30, n-1, -1):
    print(i)