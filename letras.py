# Importamos el módulo random para generar número aleatorios.
import random

# Creamos una lista para almacenar las letras del abecedario.
abecedario = []
# Este bucle toma todas las letras mayúsculas del abecedario del sistema ASCII y las mete en la lista.
for i in range(65, 91):
    abecedario.append(chr(i))

# Tomamos una letra aleatoria de la lista y la imprimimos
letra = abecedario[random.randint(0, len(abecedario) - 1)]
print(f"La letra aleatoria del abecedario del día de hoy es: {letra}")