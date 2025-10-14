#Crear una pequeña agenda en un archivo 
import os



def crear():
    with open("agenda.txt", "w") as archivo:
        return


def leer():
    try:
        with open("agenda.txt" , "r") as archivo:
            datos = archivo.readlines()
            for linea in datos:
                print("- " + linea.strip())
            input()
            return    

    except ValueError:
            print("todavia esta vacia la agenda") 
            return

def agregar():
    try:

        with open("agenda.txt" , "a") as archivo:
            mensaje = input("mensaje:  ")+" \n"
            archivo.write(mensaje)
            return
    except ValueError:
        print(" el archivo todavia no existe. crearlo")
        input()
        return     


while True:
    print("1_ crear")
    print("2- leer")
    print("3- agregar")
    print("4- salir")
    opcion = int(input("--> "))

    if opcion == 1: 
        crear()
    elif opcion == 2:
        leer()
    elif opcion == 3:
        agregar()
    else:
        break