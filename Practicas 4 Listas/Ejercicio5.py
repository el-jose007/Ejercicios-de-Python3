#Crear un gestor de tareas que pueda agregar tareas, eliminarlas o salir. usar funciones

#Agregamos la libreria para borrar pantralla
import os


def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def agregar():
    borrar_pantalla()
    print("AGREGAR TAREAS")
    print("***************") 
    if not lista:
        print("Aun no hay nada en la lista. presiona una tecla para volver al menu.")
    else:       
        for n in range(len(lista)):
            print(f"{n+1}- {lista[n]}")
    print("***************")  
    #Ingresar datos:
    print("ingrese su tarea:")
    tarea = input("--> ")
    lista.append(tarea)
    print("***************")  
    print("AGREGADA CON EXITO")
    print("***************")  
    return

def eliminar():
    borrar_pantalla()
    #Eliminar Datos:
    if not lista:
        print("Aun no hay nada en la lista. presiona una tecla para volver al menu.")
        ok = input()
        return
    else:
        for n in range(len(lista)):
            print(f"{n+1}- {lista[n]}")
            
        print("*********************")
        numero_item = int(input("--> "))
        if 0 < numero_item < n+2:
            del lista[numero_item -1]
            print("***************")  
            print("Eliminacion Exitosa! ")
            print("***************")  
            return
        else:
            print("ERROR.Ese numero no corresponde a un item")
   


#LIsta.
lista = []

#Menu

while True:
    print("***************")  
    print("Ingresar la opcion correcta:")
    print("1- Agregar tarea")
    print("2- Ver tareas agendadas")
    print("3- Eliminar Tareas")
    print("4- Salir")

    try:
        opcion= int(input("--> "))
        print("***************")  
    except ValueError:
        print("Opcion incorrecta")
        continue
    if opcion == 1:
        agregar()
    elif opcion == 2:
        if not lista:
            print("*****************")
            print("no hay elementos en la lista. agregue algunos.")
            print("*****************")
        else:
            borrar_pantalla()
            print("LISTA DE TAREAS GUARDADAS")
            print("***************")     
            for n in range(len(lista)):
                print(f"{n+1}- {lista[n]}")
            print("***************")  

    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        break       

print("Adios!!")

