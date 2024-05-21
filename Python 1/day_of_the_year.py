# Función para determinar si un año es bisiesto
def es_bisiesto(year):
    # Si el año no es divisible entre 4, no es bisiesto
    if year % 4!= 0:
        return False
    # Si el año no es un año de siglo (no divisible entre 100), es bisiesto
    elif year % 100!= 0:
        return True
    # Si el año no es divisible entre 400, no es bisiesto
    elif year % 400!= 0:
        return False
    # Si el año cumple todas las condiciones anteriores, es bisiesto
    else:
        return True

# Función para calcular el número de días en un mes
def dias_en_mes(year, month):
    # Si el año es anterior a 1582 o el mes es inválido, devuelve None
    if year < 1582 or month < 1 or month > 12:
        return None
    # Define una lista de días en cada mes (excluyendo febrero)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Calcula el número de días en el mes especificado
    res = days[month - 1]
    # Si el mes es febrero y el año es bisiesto, actualiza el número de días
    if month == 2 and es_bisiesto(year):
        res = 29
    return res


# Función para calcular el día del año
def day_of_the_year(year, month, day):
    # Inicializa el contador de días
    days = 0
    # Itera sobre los meses anteriores al mes especificado
    for m in range(1, month):
        # Calcula el número de días en el mes actual
        md = dias_en_mes(year, m)
        # Si el año o el mes es inválido, devuelve None
        if md == None:
            return None
        # Agrega los días del mes actual al contador
        days += md
    # Calcula el número de días en el mes especificado
    md = dias_en_mes(year, month)
    # Verifica si el día especificado es válido
    if day >= 1 and day <= md:
        # Devuelve el día del año
        return days + day
    else:
        # Devuelve None si el día es inválido
        return None

# Prueba la función day_of_the_year
print(day_of_the_year(2000, 12, 31))