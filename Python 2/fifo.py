class ColaError(IndexError):
    # Esta clase se utiliza para generar un error personalizado cuando la cola está vacía
    pass

class Cola:
    # Inicializar la cola con una lista vacía
    def __init__(self):
        self.__cola = []

    # Agregar un elemento al frente de la cola
    def poner(self, elem):
        self.__cola.insert(0, elem)

    # Eliminar y devolver el elemento del final de la cola
    def obtener(self):
        if len(self.__cola) > 0:
            elem = self.__cola[-1]
            del self.__cola[-1]
            return elem
        else:
            raise ColaError

# Crear un nuevo objeto Cola
cola = Cola()

# Agregar tres elementos a la cola
cola.poner(1)
cola.poner("perro")
cola.poner(False)

# Intentar eliminar y imprimir cuatro elementos de la cola
try:
    for i in range(4):
        print(cola.obtener())
except:
    print("Error en la cola")