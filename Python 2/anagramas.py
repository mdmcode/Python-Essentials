# Pide al usuario que ingrese la primera cadena
cadena_1 = input("Ingresa la primera cadena: ")

# Pide al usuario que ingrese la segunda cadena
cadena_2 = input("Ingresa la segunda cadena: ")

# Convierte la primera cadena a mayúsculas, elimina los espacios y la ordena alfabéticamente
cadenaConvertida_1 = ''.join(sorted(list(cadena_1.upper().replace(' ',''))))

# Convierte la segunda cadena a mayúsculas, elimina los espacios y la ordena alfabéticamente
cadenaConvertida_2 = ''.join(sorted(list(cadena_2.upper().replace(' ',''))))

# Verifica si la longitud de la primera cadena ordenada es mayor que cero y coincide con la segunda cadena ordenada
if len(cadenaConvertida_1) > 0 and cadenaConvertida_1 == cadenaConvertida_2:
    # Imprime que las cadenas son anagramas
    print("Anagramas")
else:
    # Imprime que las cadenas no son anagramas
    print("No son anagramas")