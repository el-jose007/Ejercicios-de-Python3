#Pide un número (ej. 123) y suma sus dígitos: 1+2+3 = 6.

numero = input("ingrese su numero : ")

resultado = 0
for i in numero:
    if i.isdigit():
        resultado += int(i)

print("el resultado es: ", resultado)
