'''Ejercicio 4: Registro de usuarios con validación 

Pide nombre, edad y correo. Valida: 

    Nombre: solo letras
    Edad: número entre 1 y 120
    Correo: debe tener "@" y ".com"
''' 

# ingresar los valores
# Validar.
# No voy a dejar que siga al siguiente parametro si no completo el anterior. 

# Nombre: 
while True:
    try:
        print("Ingrese su nombre: ")
        nombre = input("--> ")
        if nombre.isalpha():
            break
        else:
            print("El nombre esta mal ingresado")
    except ValueError:
        print("Dato no valido")
        continue

# Edad

while True:
    try:
        print("Ingrese su edad: ")
        edad = input("--> ")
        if edad.isdigit(): # <-------------------------------------- Linea para corregir
            if 1 > int(edad) >= 121:
                print("Error. imposible tener esa edad")
            else:
                break
    except ValueError:
        print("ERROR. Dato invalido")

# Correo electronico: 

while True:
    try:
        print("Ingrese el correo eletronico:")
        correo = input("--> ")

        #Verificamos Si tiene @
        if "@" and ".com" in correo:
            break
        else:
            print("Error. formato de mail incorrecto")
    except ValueError:
        print("ERROR. ingreso invalido")

print(f"nombre: {nombre}")
print(f"Edad: {edad}")
print(f" Correo electronico: {correo}")





