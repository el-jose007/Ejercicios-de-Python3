#Pide un número N y muestra todos los pares desde 1 hasta N.

numero = int(input("Dame un numero: "))

acumulador = 0
pares = []
for i in range(2,numero+1,1):
    if i%2 == 0:
        acumulador +=1
        pares.append(str(i))
print(f" desde el 1 al {numero} hay {acumulador} numeros pares")
print("los pares son: ", ", ".join(pares))