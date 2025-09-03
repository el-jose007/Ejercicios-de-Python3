#Hacer algo una y otra vez... hasta que la condición sea False

respuesta = None
while respuesta != "python":
    respuesta = input("¿Cual es el mejor lenguaje de programacion?: ").lower()
    if respuesta == "python":
        print("Excelente respuesta")
    else:
        print("Noooo, pensa bien...")

