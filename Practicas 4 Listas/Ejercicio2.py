'''
Ejercicio 2: Promedio de notas (con lista)
Pide cuántas notas, pídelas una por una y calcula el promedio.'''

#
print("ingrese sus Notas. (Presione una letra para finalizar)")
notas=[]
promedio = 0

while True:
    dato = input("Nota:  ")
    if dato.isalpha():
        break
    else:
        notas.append(float(dato))

if len(notas) > 1:
    for i in range(len(notas)):
        promedio += notas[i]
    print(f"Promedio de {len(notas)} es {promedio/len(notas)}")
else:
    print("no hay suficientes notas. ")