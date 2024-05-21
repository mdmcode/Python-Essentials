# Ingresa el texto a encriptar.
texto = input("Ingresa un mensaje: ")

# Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
valor_cambio = 0

while valor_cambio == 0:
    try:    
        valor_cambio = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if valor_cambio not in range(1,26):
            raise ValueError
    except ValueError:
        valor_cambio = 0
    if valor_cambio == 0:
        print("¡Valor de cambio inválido!")

cifrado = ''

for caracter in texto:
    # ¿Es un letra?
    if caracter.isalpha():
        # Cambia su código.
        codigo = ord(caracter) + valor_cambio
        # Encontrar el código de la primera letra (mayúscula o minúscula).
        if caracter.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Realizar corrección.
        codigo -= first
        codigo %= 26
        # Agregar carácter codificado al mensaje.
        cifrado += chr(first + codigo)
    else:
        # Agregar carácter original al mensaje.
        cifrado += caracter

print(cifrado)