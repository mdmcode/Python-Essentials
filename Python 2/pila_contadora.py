class Pila:
    # Inicializar la pila con una lista vacía
    def __init__(self):
        self.__pila = []

    # Agregar un elemento a la parte superior de la pila
    def empujar(self, val):
        self.__pila.append(val)

    # Eliminar y devolver el elemento superior de la pila
    def pop(self):
        val = self.__pila[-1]
        del self.__pila[-1]
        return val

class ContadorPila(Pila):
    # Inicializar la pila de conteo con un contador establecido en 0
    def __init__(self):
        Pila.__init__(self)
        self.__contador = 0

    # Devolver el valor actual del contador
    def obtener_contador(self):
        return self.__contador

    # Incrementar el contador y eliminar el elemento superior de la pila
    def pop(self):
        self.__contador += 1
        return Pila.pop(self)

# Crear un nuevo objeto ContadorPila
stk = ContadorPila()

# Empujar y sacar 100 elementos de la pila
for i in range(100):
    stk.empujar(i)
    stk.pop()

# Imprimir el valor final del contador
print(stk.obtener_contador())