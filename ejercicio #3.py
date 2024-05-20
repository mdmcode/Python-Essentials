# Haz un programa que pida tres números al usuario y muestre por pantalla cuál es el
# mínimo y cuál es el máximo y que indique si son pares o impares. No uses listas.

primerNumero = int(input("Primer numero: "))
segundoNumero = int(input("Segundo numero: "))
tercerNumero = int(input("Tercer numero: "))

if primerNumero > segundoNumero and primerNumero > tercerNumero:
    print(f'{primerNumero} es el mayor')
elif segundoNumero > primerNumero and segundoNumero > tercerNumero:
    print(f'{segundoNumero} es el mayor')
elif tercerNumero > primerNumero and tercerNumero > segundoNumero:
    print(f'{tercerNumero} es el mayor')

if primerNumero < segundoNumero and primerNumero < tercerNumero:
    print(f"{primerNumero} es el menor")
elif segundoNumero < tercerNumero and segundoNumero < primerNumero:
    print(f"{segundoNumero} es el menor")
elif tercerNumero < segundoNumero and tercerNumero < primerNumero:
    print(f"{tercerNumero} es el menor")

numerosPares = ''
numerosImpares = ''

if primerNumero % 2 == 0:
    numerosPares += str(primerNumero) + ' '
else:
    numerosImpares += str(primerNumero) + ' '

if segundoNumero % 2 == 0:
    numerosPares += str(segundoNumero) + ' '
else:
    numerosImpares += str(segundoNumero) + ' '

if tercerNumero % 2 == 0:
    numerosPares += str(tercerNumero) + ' '
else:
    numerosImpares += str(tercerNumero) + ' '

if numerosPares != '':
    print(f"Los numeros pares son {numerosPares}")
else:
    print("No hay números pares")

if numerosImpares != '':
    print(f"Los numeros impares son {numerosImpares}")
else:
    print("No hay números impares")