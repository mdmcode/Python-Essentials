from datetime import datetime

# Usamos la función datetime con el año, mes, día, hora, minutos
my_date = datetime(2024, 6, 6, 16, 48)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Día de la semana: %w"))
print(my_date.strftime("Día del año: %j"))
print(my_date.strftime("Número de semana en el año: %W"))