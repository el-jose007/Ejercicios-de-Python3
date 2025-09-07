#Pide números al usuario. Suma solo los positivos. Si ingresa un negativo, termina.

print("ingresar numeros como loco")
acumulador = 0
while True:
    numero=float(input("---->"))
    if numero < 0:
        print("programa terminado. ")
        print(f"La suma es {acumulador}")
        break
    else:
        acumulador += numero
