#Haz una cuenta regresiva desde 10 hasta 1, y luego: "¡Despegue!"

try:
    cuenta=int(input("desde que nuemro desea contar?"))
    if 0 < cuenta < 20:
        for i in range(cuenta,0,-1):
            print(str(i)+"!")
    else:
        print("estas fuera del rango")

except ValueError:
    print("Ingresaste un error") 


