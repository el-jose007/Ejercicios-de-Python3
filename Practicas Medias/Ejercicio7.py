#El usuario tiene 3 intentos para escribir la contraseña "python123".

print("ingrese la contraseña. tiene 3 intentos")
passw= "python3"

for i in range(3):
    ingreso = input("-->").lower()
    if ingreso == passw:
        print("siii, perfecto")
        break
    else:
        print("Incorrecto")
else:
    print("demasiados intentos. cerrando")


