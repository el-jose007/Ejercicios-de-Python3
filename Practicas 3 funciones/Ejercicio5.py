# crear un programa que salude de la manera adecuada segun la hora 
#que es. 

from datetime import datetime

def saludar(hs):
    if 20<= hs < 24 or 0 <= hs <6:
        return "buenas noches"
    elif 6 <= hs < 12:
        return "buenos dias"
    elif 12<= hs < 20:
        return "buenas tardes"
               
#la hora actual
hora = datetime.now().hour

print(saludar(hora))
print("Son las ", hora)

