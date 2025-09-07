#Invertir una palabra (sin [::-1])

#Version prohibida
palabra = input("Ingresa la plabra: ")
letras = len(palabra)

#geenrar el string al reves.
Acumulador ="" 
for i in range(letras-1, -1, -1):
    Acumulador += palabra[i]
print("Al reves seria ", Acumulador)


#Version mas eficiente:
invertido =""
for letra in palabra:
    invertido = letra + invertido

print(invertido)