#Simulador de dado .Lanza un dado (1-6) hasta que salga un 6. 

import random

print("dado digital")
while True:
    numero = random.randint(1,6)
    if numero == 6:
        break
    else:
        print(numero)
