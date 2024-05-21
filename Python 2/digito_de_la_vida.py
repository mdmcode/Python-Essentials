fecha = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
"""
Input para obtener la fecha de cumpleaños del usuario con un formato específico.
El formato puede ser AAAAMMDD o AAAADDMM, y debe tener exactamente 8 dígitos.
"""

if len(fecha)!= 8 or not fecha.isdigit():
    print("Formato de fecha inválida.")
    """
    Verifica si la fecha de cumpleaños ingresada tiene un formato inválido.
    Si la longitud de la fecha es diferente a 8 caracteres o contiene caracteres no numéricos, se muestra un mensaje de error.
    """

else:
    while len(fecha) > 1:
        la_suma = 0
        """
        Inicializa una variable para almacenar la suma de los dígitos de la fecha.
        """
        for dig in fecha:
            la_suma += int(dig)
            """
            Itera sobre cada dígito de la fecha y lo suma a la variable "the_sum".
            """
        print(fecha)
        fecha = str(la_suma)
        """
        Imprime la fecha actual y la reemplaza con la suma de sus dígitos.
        """
    print("Tu Dígito de la Vida es: " + fecha)
    """
    Finalmente, imprime el Dígito de la Vida, que es la suma reducida de los dígitos de la fecha de cumpleaños.
    """