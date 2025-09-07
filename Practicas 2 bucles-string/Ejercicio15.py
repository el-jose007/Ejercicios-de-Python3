#Pide una palabra y cuenta cuántas vocales tiene.

vocales = "aeiou"
palabra = input("ingrese la palabra: ")

#Analisis
acumulador = 0
for i in palabra:
    for letra in vocales:
        if letra == i:
            acumulador += 1

print(f"tiene {acumulador} vocales")


#Version 2

acumulador2 = 0

for letra in palabra:
    if letra in vocales:
        acumulador2 += 1

print(f"tiene {acumulador2} vocales")
