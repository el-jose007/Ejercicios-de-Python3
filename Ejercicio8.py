#Ejercicio: Pide nombre y apellido, y muestra las iniciales.

nombre = input("ingresar tu nombre: ").split()

for i in range(2):
    Mayuscula= (nombre[i].capitalize())
    print(Mayuscula[:1])
iniciales =""
#Otra forma:
nombre =input("De vuelta: ").split()
for i in range (2):
    iniciales += nombre[i][0]
print(iniciales.upper()) 


