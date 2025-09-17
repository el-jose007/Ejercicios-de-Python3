# Ingresar una frase a al programa y luego mostrar las palabras intertidas en orden


#ingresar datos

frase = input("¿Cual es tu frase?")
nueva_frase =""
#Dividir la cadena en palabras. 
palabras =frase.split()
#recorres la frase al reves
for i in palabras[::-1]:
    nueva_frase += i + " "

print(nueva_frase)
