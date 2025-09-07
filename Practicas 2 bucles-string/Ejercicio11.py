#Pide un texto, quita espacios, convierte a minúsculas y verifica si es "hola".

# ingresar las palabras, dicidirlas el una lista y quietar espacios 
# transformando automaticamente a minusculas 
frase = input("ingresa un texto: ").lower()
sin_espacios = frase.split()

#Verrificar
nueva_frase =""
for i in sin_espacios:
    if i == "hola":
        print("Contiene la palabra hola")

    nueva_frase += i

print(nueva_frase)
