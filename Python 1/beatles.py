# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles = []

print("Bienvenido al programa de información sobre The Beatles")
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Ahora debes ingresar los miembros de la banda que no fueron permanentes y dejaron la banda al poco tiempo.")
print("Estos miembros fueron: Stu Sutcliffe y Pete Best. En ese orden.")

for i in range(2):
    beatles.append(input("Ingresa el miebro de la banda faltante: "))

del beatles[3]
del beatles[3]

beatles.insert(0, "Ringo Starr")
print("Los miembros finales de la banda fueron: ", beatles)