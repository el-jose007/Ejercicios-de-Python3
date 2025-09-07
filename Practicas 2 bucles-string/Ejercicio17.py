#Pide un número y dibuja una pirámide con ese número de filas.

# limitar las filas.
try:
    numero = int(input("ingresar el numero: "))
except ValueError: 
    print("error al ingresar el dato.")

# trabajar con  las secuencias multiplicando los char por el numero ingresado pero en orden ascendente.

for i in range(1,numero):
    print("*" * i)


