'''Editor de perfil interactivo 

Situación:
Quieres que el usuario pueda crear y modificar su propio perfil paso a paso. 

Objetivo:
Hacer un menú interactivo que permita editar cualquier campo del perfil. 

Instrucciones:   

    Inicia un perfil con claves vacías.  
    En un bucle, pregunta qué clave quiere modificar.  
    Si elige una válida, pide el nuevo valor y actualízala.  
    Si escribe "salir", termina.
     '''

#Crear el perfil.
perfil = {
    'nombre':'Juan',
    'apellido': 'Dominguez',
    'edad' : 15
}

#Preguntar si quiero editar algo

while True:
    clave = input("¿Qué quieres modificar? (nombre/apellido/edad/salir): ").lower()
    if clave == 'salir':
        print("Adios")
        break
    elif clave == 'nombre':
       print("Nombre actual: ",perfil['nombre'])
       nuevo_nombre = input('Nuevo nombre: ')
       perfil['nombre'] = nuevo_nombre
       break
    elif clave == 'apellido':
       print(f"Apellido actual {perfil['apellido'].capitalize()}")
       nuevo_apellido = input("Nuevo apellido")
       perfil['apellido'] = nuevo_apellido
       break
    elif clave == 'edad':
        print(f"Edad actual {perfil['edad'].capitalize()}")
        nuevo_edad = input("Nueva edad")
        perfil['apellido'] = nuevo_edad
        break
    else:
        print("opcion incorrecta")
        break
       

''' 
MAS EFICIENTE:

while True:
    print(f"\nPerfil actual: {perfil}")
    clave = input("¿Qué quieres modificar? (nombre/edad/ciudad/salir): ").lower()

    if clave == "salir":
        print("✅ Perfil guardado. ¡Hasta luego!")
        break
    elif clave in perfil:
        nuevo = input(f"Nuevo valor para '{clave}': ")
        perfil[clave] = nuevo
        print(f"✔️ '{clave}' actualizado.")
    else:
        print("❌ Clave no válida. Intenta de nuevo.")'''



#Resolverlo
