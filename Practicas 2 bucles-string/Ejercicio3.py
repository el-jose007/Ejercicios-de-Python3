#Generar un numero del 1 al 10 de manera aleatoria y 
# darle al  jugador 3 oportunidades de adivinarlo
#Utilizamos WHILE

import random

numero_secreto = random.randint(1,10)
numero = int(input("ingrese un numero del uno al diez: "))

#Compobar con 3 intentos
contador = 2
while contador !=0:
    if numero == numero_secreto:
        print(f"Siiii, adivinaste!!! era el {numero_secreto}")
        break
    else:
        print("No, no es ese, intenta una vez mas...")
        contador-=1
        numero = int(input("el numero es: "))
if contador == 0:
    print("No, era ese y se te acabaron los intentos")
