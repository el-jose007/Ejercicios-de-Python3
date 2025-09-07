#ide una palabra y verifica si es un palíndromo 
# (se lee igual al derecho y al revés). Ej: "reconocer".

palabra = input("ingrese la palabra: ")

#Version 1
print("***VERSION 1***")
inversa = palabra[::-1]
if palabra == inversa:
    print("es un palindromo")
else:
    print("No es un palindromo")

#Version 2 con iteracciones

print("**VERSION 2***")
inversa2 = ""

for letras in palabra:
    inversa2 = letras + inversa2

if palabra == inversa2:
    print("es un palindromo")
else:
    print("No es un palindromo")

#Version 3 (cada vez peor jajaj)
print("**VERSION 3***")
Numeroletras = len(palabra)
inversa3 = ""
for i in range (Numeroletras-1,-1,-1):
    inversa3 += palabra[i]

if palabra == inversa3:
    print("es un palindromo")
else:
    print("No es un palindromo")


