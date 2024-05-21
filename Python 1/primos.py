"""
Tu tarea es escribir una función que verifique si un número es primo o no.

La función:

se llama is_prime;
toma un argumento (el valor a verificar)
devuelve True si el argumento es un número primo, y False de lo contrario.
"""

# Definimos la funcion que analiza si el numero es primo
def is_prime(n):
    # Si el numero es menor que 2, no es primo
    # Recorremos todos los numeros desde dos hasta la raiz cuadrada de n
    for i in range(2, int(1 + n**0.5)):
        # Si n es divisible entre alguno de estos numeros, no es primo
        if n % i == 0:
            return False
    # Si n no es divisible por ninguno de los numeros entonces es primo
    return True

# Analiza cuales numeros del 2 al 20 son primos
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")