'''Ejercicio 1: Analizador de Frases
Pide una frase y muestra:

* Número de caracteres (sin espacios)
* Número de palabras
* Cuántas vocales tiene
* La frase en mayúsculas y al revés'''

# escribir una frase, limpiar
vocales = "AEIOU"
cant_vocales = 0
caracteres = ""

#ingreso:
frase = input("ingresa tu frase: ").upper() #ingreso y mayusculas de una.

#¿Cuantas palabras? 
print(f"hay {len(frase.split())} palabras")
#¿Cuantas vocales? 
caracteres = frase.replace(" ", "")
print(f"Tiene {len(caracteres)} caracteres")
#¿Cuantas vocales? 
for letras in caracteres:
    if letras in vocales:
        cant_vocales += 1
print(f"Tiene {cant_vocales} vocales")
#mostrar al reves
print("Al reves seria: ", caracteres[::-1])



