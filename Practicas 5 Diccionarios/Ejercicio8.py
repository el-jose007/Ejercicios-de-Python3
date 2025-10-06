#Agendita guiada con Deepseek.
import os
#Crear una agenda paso a paso con python y deepseek.
def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def mostrar():
    if agenda: 
        for contacto in agenda:
            print(f"Nombre: {contacto['nombre']}")
            print ("Teléfono:", contacto['telefono'])
            print("email: " , contacto['email'])
    else:
        print("la agenda esta vacia ")
        
def busquedas():
    nombre_buscar = input("nombre del contacto:").lower()
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre_buscar:
            print("*" *20)
            print(f"Nombre: {contacto['nombre']}")
            print ("Teléfono:", contacto['telefono'])
            print("email: " , contacto['email'])
            print ("*" *20)
            return
    print("contacto no encontrado")
    
def modificar():
    nombre_editar = input("que nombre desea editar").lower()
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre_editar:
            print("1- editar nombre.")
            print("2- editar teléfono")
            print("3- editar email")
            opcion = int(input("--> "))
            if opcion == 1:
                contacto['nombre'] = input("--> ")
                print("listo")
                return
            elif opcion == 2:
                contacto['telefono'] = int(input("--> "))
                print("listo")
                return
            elif opcion == 3:
                contacto['email'] = input("--> ")
                print("listo")
                return
    print('contacto no encontrado')
             
                
def eliminar():
    nombre_eliminar = input("que nombre desea editar").lower()
    for contacto in agenda:
        if contacto['nombre'].lower() == nombre_eliminar:
            print("esta seguro? (s/n)" )
            opcion = input("--> ").lower()
            if opcion == "s":
                agenda.remove(contacto)
                return
            else:
                print("Cancelado.")
                print("*" *20)
                return

def agregar():
    nombre_nuevo = input("Nombre: ")
    telefono_nuevo = int(input("Telefono: "))
    email_nuevo = input("Email: ") 

    contacto_nuevo ={
        "nombre" : nombre_nuevo,
        "telefono" : telefono_nuevo,
        "email" : email_nuevo
    }

    agenda.append(contacto_nuevo)
    
    
agenda = [
    
] #<-- lista vacia.


# Menu

while True:
    borrar_pantalla()
    print("Agenda personal: ")
    print("*" *20)
    print("1- para ver contactos")
    print("2- Para agregar contactos")
    print("3- para buscar un contacto")
    print("4- para editar ")
    print("5- para Eliminar contacto.")
    print("6- Para salir")

    try: 
        opcion = int(input("--> "))
    except ValueError:
        print(" opcion invalida")
        continue
    if opcion == 1:
        mostrar()
        input("presione una tecla...")
    elif opcion == 2:
        agregar()
        input("presione una tecla...")

    elif opcion == 3:
        busquedas()
        input("Presiona una tecla...")

    elif opcion == 4:
        modificar()
        input("presione una tecla...")
    elif opcion == 5:
        eliminar()
        input("Presione una tecla..")
    elif opcion == 6:
        borrar_pantalla()
        print("*" *20)
        print("      ¡ADIOS!")
        print("*" * 20)
        break



