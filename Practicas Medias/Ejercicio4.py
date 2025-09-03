##Generar un numero del 1 al 10 de manera aleatoria y 
# darle al  jugador 3 oportunidades de adivinarlo
#Utilizamos WHILE

import random

numero_secreto = random.randint(1,10)

for i in range(3,0,-1):
    numero = int(input(f"Ingreso numero {i}:"))
    if numero_secreto == numero:
        print(f"Exacto! era el {numero_secreto}")
        break
else:
    print(f"Se te acabaron los intentos... era el {numero_secreto}")
