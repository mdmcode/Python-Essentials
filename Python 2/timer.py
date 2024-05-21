# Definimos una función para que el número que se muestre siempre tenga dos dígitos.
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

# Creamos la clase Timer
class Timer:
    # El constructor toma los parámetros hours, minutes y seconds y los privatiza
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    # Se crea un método privado para convertir hour, minutes y seconds en cadena.
    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    # Este método establece los límites de las horas, minutos y segundos.
    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    # Este método muestra la unidad de tiempo anterior a la actual.
    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

# Se instancia la clase
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)