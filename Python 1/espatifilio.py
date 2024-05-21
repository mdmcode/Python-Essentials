# Tomar la entrada del usuario
entrada = input("Ingrese el nombre de la flor: ")

# Ejecución condicional
if entrada.upper() == "ESPATIFILIO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada.lower() == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print(f"¡Espatifilo!, ¡No {entrada}!")