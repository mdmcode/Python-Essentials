""""
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene 
un bloque más que la capa superior.
"""
# Leer la cantidad de bloques del usuario
bloques = int(input("Introduce la cantidad de bloques: "))

# La altura de la pirámide es el entero más grande tal que
# (capas*(capas+1))/2 <= n_bloques
capas = 0
while (capas*(capas+1))/2 <= bloques:
    capas += 1

# Imprimir la altura de la pirámide
# Se le resta a la cantidad de capas la capa que no pudo completar
print("La cantidad de capas es: ", capas - 1)