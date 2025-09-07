#Pide el total de la cuenta y el porcentaje de propina. 
# Calcula cuánto debe dejar de propina y el total a pagar.

try:
    cuenta = float(input(" ingrese la cuenta: "))
    propina = cuenta * 0.1
    print(f"La propina para su cuenta de ${cuenta} es de ${propina}")
except ValueError:
    print("opcion incorrecta")