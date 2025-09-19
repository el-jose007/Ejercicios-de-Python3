#Contador de palabras en una frase

def descomponer(frase):
    conversion = frase.split()
    return conversion



#ingresar frase:
frase = input("ingresar una frase: ")

palabras = descomponer(frase)
for c in palabras:
    print (c)

