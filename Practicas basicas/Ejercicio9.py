"""Pide peso (kg) y altura (m). Calcula el IMC: IMC = peso / (altura ** 2)
Y muestra:

<18.5 → Bajo peso
18.5–24.9 → Normal
25–29.9 → Sobrepeso
≥30 → Obesidad"""
try:

#Conocer el Peso y la altura
    peso = float(input("Ingrese el peso: "))
    altura = float(input("Ingresa tu altura: "))
#Realizar el calculo
    imc = peso / (altura **2)
#Categorizar segun el IMC
    if imc >= 30:
        print(f"Con tu altura {altura}m y tu peso de {peso}kg, tu IMC es de {imc} que correspone a un hombre con Obecidad")
    elif imc >=25:
        rint(f"Con tu altura {altura}m y tu peso de {peso}kg, tu IMC es de {imc} que correspone a un hombre con Sobrepeso")
    elif imc >= 18.5:
        rint(f"Con tu altura {altura}m y tu peso de {peso}kg, tu IMC es de {imc} . Corresponde a un hombre NORMAL")
    else:
        print("estas bajo de peso")
except ValueError:
   print("Ha ingresado un valor incorrecto")