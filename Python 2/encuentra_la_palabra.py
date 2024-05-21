word = input("Ingresa la palabra que deseas encontrar: ").upper()
#Solicita al usuario que ingrese una palabra y la convierte a mayúsculas.

strn = input("Ingresa la cadena en donde deseas buscar: ").upper()
#Solicita al usuario que ingrese una cadena y la convierte a mayúsculas.

found = True
#Inicializa una variable para indicar si la palabra se encuentra en la cadena.

start = 0
#Inicializa una variable para indicar el índice de inicio para la búsqueda.

for ch in word:
    pos = strn.find(ch, start) 

    #Busca la posición de cada carácter de la palabra en la cadena, comenzando desde el índice de inicio.

    if pos < 0:
        found = False
        break
    start = pos + 1

    #Actualiza el índice de inicio para la próxima búsqueda.
    #Si no se encuentra el carácter, se establece found en False y se sale del ciclo.


if found:
    print("Si")

    #Imprime "Si" si la palabra se encuentra en la cadena.

else:
    print("No")

    #Imprime "No" si la palabra no se encuentra en la cadena.
