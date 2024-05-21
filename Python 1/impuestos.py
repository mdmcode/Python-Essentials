# Tomar el ingreso como entrada
ingreso = float(input("Ingrese el ingreso: "))

# Calcular el impuesto
if ingreso <= 85528:
    impuesto = round(0.18 * ingreso - 556.02, 0)
else:
    impuesto = round(14839.02 + 0.32 * (ingreso - 85528), 0)

# Imprimir el impuesto
if impuesto < 0:
    print("No hay impuesto.")
else:
    print(f"El impuesto es de {impuesto} pesos.")