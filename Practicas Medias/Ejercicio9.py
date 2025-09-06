#Contar las letras "A" de una cadena, sean o no mayusculas.

#ingresar la palabra. 

palabra = input("ingresar la palabra").upper()
Contador=0

for i in palabra:
    if i == "A":
        Contador +=1

print(f"la palabra tiene {Contador} letras A")

