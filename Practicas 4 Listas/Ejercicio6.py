'''Ejercicio 7: Invertir una lista 

Sin usar .reverse()'''


#crear la lista_
lista =[]
lista2=[]

for a in range(10):
    item = input()
    lista.append(item)

for a in range (len(lista)-1 ,-1,-1):
    lista2.append(lista[a])

print(lista2)
