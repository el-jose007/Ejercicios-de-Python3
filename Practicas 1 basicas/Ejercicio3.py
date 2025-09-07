#Crear una calculadora utilizando el codigo python 

#Mostrar datos: 
print("Elegir en tipo de operacion: ")
print("1- suma")
print("2- resta")
print("3 - multiplicacion")
print("4- Exponentes")

try: 

    eleccion = int(input())
    if eleccion == 1:
        num1= int( input("ingresa el primer numero: "))
        num2 =int( input("ingrese el segundo: "))
        resultado= num1 + num2
        print("el resultado es: ", resultado)

    elif eleccion == 2:
        num1= int( input("ingresa el primer numero: "))
        num2 =int( input("ingrese el segundo: "))
        resultado =  num1 - num2
        print("el resultado es: ", resultado)
    elif eleccion == 3:
        num1= int( input("ingresa el primer numero: "))
        num2 =int( input("ingrese el segundo: "))
        resultado = num1 * num2
        print("el resultado es: ", resultado)
    elif eleccion == 4:
        num1= int( input("ingresa numero: "))
        num2 =int( input("ahora su exponente: "))
        resultado = num1 ** num2
        print("el resultado es: ", resultado)
    else:
        print("opcion no valida")

except ValueError:
    print("debe ingresar una opcion valida")
