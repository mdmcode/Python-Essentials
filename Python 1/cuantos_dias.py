# Función para verificar si un año es bisiesto
def es_bisiesto(year):
    # Si el año no es divisible por 4, no es bisiesto
    if year % 4!= 0:
        return False
    # Si el año no es un año de siglo (no divisible por 100), es bisiesto
    elif year % 100!= 0:
        return True
    # Si el año no es divisible por 400, no es bisiesto
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


# Años y meses de prueba
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = dias_en_mes(yr, mo)
    # Verifica si el resultado calculado coincide con el resultado esperado
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")