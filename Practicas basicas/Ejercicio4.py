#Calcular el Area de un circulo
try:
    radio =float(input("radio "))
    resultado = 3.1415 * (radio**2)
    print("la seccion es: ", resultado)

except ValueError:
    print("Ingresaste cualquier Cosa!!")