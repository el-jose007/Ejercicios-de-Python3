#Ejercicio 3: calcular el area de un circulo

def area(radio):
    area = math.pi *  (radio**2)
    return area

import math

radio = float(input("Ingrese el valor del radio: "))
print(f" el radio es: {radio} y el area es {area(radio):.3f}") #Aca redondeamos a 3 decimales
      



