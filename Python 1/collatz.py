"""
1. toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
2. si es par, evalúa un nuevo c0 como c0 ÷ 2;
3. de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
4. si c0 ≠ 1, salta al punto 2.

Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea 
diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. 
Tu código también debe mostrar todos los valores intermedios de c0.
"""

# Leer el número natural dado
n = int(input("Introduce un número natural: "))

# Inicializar el contador de pasos en 0
pasos = 0

# Bucle while que se ejecuta hasta que c0 sea 1
while n != 1:
    # Imprimir el valor actual de c0
    print(n)

    # Incrementar el contador de pasos en 1
    pasos += 1

    # Evaluar el nuevo valor de c0
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

# Imprimir el valor final de c0 y el número de pasos necesarios
print(n)
print("Número de pasos:", pasos)