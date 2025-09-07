#La computadora elige una palabra, la invierte y el usuario debe adivinar la original.

import random

palabras = ["dientudo","bagre", "palometa","surubi","carpa"]

#Elegimos palabra

palabra_ramdon = random.choice(palabras) #aca elijo una al azar
reves = palabra_ramdon[::-1] #la invertimos

#preguntamos
print ("¿que dice aca?", reves)
respuesta = input("dice: ")
if respuesta == palabra_ramdon:
    print("Siiii, la palabra era ", palabra_ramdon)
else:
    print("No, la palabra corecta era: ", palabra_ramdon)
    


