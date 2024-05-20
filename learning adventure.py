import random

### Listas de preguntas ###
ingles = [['Traduce: CASA', 'House'], 
            ['Traduce: CARRO', 'car'], 
            ['Traduce: MADRE', 'Mom'],
            ['Traduce: MANZANA', 'Apple'],
            ['Traduce: HABITACIÓN', 'Room'],
            ['Traduce: AZÚCAR', 'Sugar']
        ]
mates = [['Raíz cuadrada de 9', '3'], 
        ['2 + 2', '4'], 
        ['2 X 4', '8'],
        ['¿Cuantos segundos hay en un minuto?', '60'],
        ['2 X 2 + 10', '14'],
        ['¿Cuantos angulos tiene un triangulo?', '3'],
        ['El único numero primo par', '2']
        ]

general = [['¿Cuantos huesos tiene\n el cuerpo humano?', '206'], 
            ['¿Cuanto acabó la\n segunda guerra mundial', '1945'], 
            ['¿En que fecha se celebra\n la independencia en Colombia?', '20 de Julio'],
            ['¿En que año se\n descubrió América?', '1492'],
            ['¿Cual es el pais mas\n grande del mundo?', 'Rusia'],
            ['¿Cual es el animal más\n grande del planeta?', 'Ballena azul'],
            ['¿Cual es la capital\n de Colombia?', 'Bogotá']
            ]

opcionesIngles = [['Hosing', 'House', 'Tree'], 
                  ['Audi', 'Wheel', 'Car'],
                  ['Mom', 'Mami', 'Nana'],
                  ['Apple', 'Mango', 'Apol'],
                  ['Habitation', 'Room', 'Living'],
                  ['Sweet', 'Sour', 'Sugar']]

opcionesMates = [['9', '3', 'No tiene'],
                 ['4', '2', '7'],
                 ['16', '70', '8'],
                 ['80', '60', '100'],
                 ['24', '38', '14'],
                 ['3', '180', '360'],
                 ['6', '2', '8']]

opcionesGeneral = [['365', '206', '50'],
                   ['2004', '1845', '1945'],
                   ['7 de agosto', '1 de Enero', '20 de julio'],
                   ['1492', '1955', '2018'],
                   ['China', 'Rusia', 'Colombia'],
                   ['Ballena azul', 'Elefante', 'Hormiga'],
                   ['Cali', 'Bogotá', 'Buenaventura']]

pregunta = ''
preguntasUsadas = []
opciones= []
respuesta = ''
fila = 0
preguntas = []

# Toma un parametro con el nombre de la materia o conjunto de palabras
def obtenerLista(lista):
    global preguntas, opciones
    if lista == 'ingles':
        preguntas = ingles
        opciones = opcionesIngles
    elif lista == 'matematicas':
        preguntas = mates
        opciones = opcionesMates
    elif lista == 'cultura general':
        preguntas = general
        opciones = opcionesIngles

def obtenerPregunta():
    global pregunta, opcionesElegidas, respuesta, fila, preguntasUsadas, preguntas
    #Compara el parametro con las listas existentes
    fila = random.randint(0, len(preguntas))
    opcionesElegidas = opciones[fila]
    pregunta = preguntas[fila][0]     
    respuesta = preguntas[fila][1]

    print(pregunta)

    if pregunta in preguntasUsadas:
        pass
    else:
        preguntasUsadas.append(pregunta)

    preguntas.remove(preguntas[fila])

    return respuesta

vidaDragon = 100
vidaJugador = 100

def obtenerOpciones():
    print(opcionesElegidas[0])
    print(opcionesElegidas[1])
    print(opcionesElegidas[2])

def comprobarVictoria(rJugador, r):
    global vidaJugador, vidaDragon
    if rJugador.lower() == r.lower():
        print("¡Correcto!")
        vidaDragon = vidaDragon - 5
        print(f"Atacaste al dragon, tiene {vidaDragon} de vida")
    else:
        print("Incorrecto")
        vidaJugador = vidaJugador - 5
        print(f"Te han atacado, tiene {vidaJugador} de vida")

opcion = ''
materia = ''

print("¿Que materia desea escoger?\n Ingles\n Matematicas\n Cultura General\n")
materia = input()
obtenerLista(materia)

while vidaDragon > 0 and vidaJugador > 0:
    respuesta = obtenerPregunta()
    obtenerOpciones()
    respuestaJugador = input()
    comprobarVictoria(respuestaJugador, respuesta)

if vidaDragon == 0:
    print("Tú ganas")
elif vidaJugador == 0:
    print("El dragón gana")
