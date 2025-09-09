# Crea una función que reciba nombre y edad, y devuelva un saludo con ambas.

def saludo (nombre, edad):
    return f"Hola {nombre}! tenes {edad} años"

print("Ingresa tu nombre y tu edad")
nom = input("-->")
ed = int(input("-->"))

print(saludo(nom,ed))

