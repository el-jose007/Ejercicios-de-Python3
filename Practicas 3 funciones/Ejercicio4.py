#Ejercicio 5: Conversor de temperatura (con funciones)
# Ejercicio 5: Conversor de temperatura (con funciones)

# funciones:
def a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ingresar datos:
try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Presione C si está en Celsius o F si está en Fahrenheit: ").upper()
    
    if unidad == "C":
        print("En Fahrenheit:", a_fahrenheit(temperatura))
    elif unidad == "F":
        print("En Celsius:", a_celsius(temperatura))
    else:
        print("Unidad incorrecta")
except ValueError:
    print("Dato inválido")

