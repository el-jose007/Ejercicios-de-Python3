'''Sistema de Gestion de biblioteca:
1)Agregar libros nuevos
2) Listar los libros
3) Buscar libros por titulo o autor
4) Prestar libro (cambiar disponible a false)
5) devolver libro (cambiar disponibilidad a True)
6) Eliminar libro
7) Salir

libro = {
    "titulo": ""
    "autor": "",
    "ano": "",
    "disponible: True
    }
'''
import os

def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#creamos lista vacia

biblioteca = []

# creamos la funcion agregar libro
def agregar():
    nombre = input("Nombre del libro: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    
    libro_nuevo= {
        "titulo" : nombre,
        "autor" : autor,
        "anio" : anio,
        "disponible" : True
        }
    
    biblioteca.append(libro_nuevo)
    print("*" * 10)
    input("Presiona una tecla")


#mostrar libros de la biblioteca    
def mostrar_biblioteca(): 
    titulo = ""
    if biblioteca:
        #recorremos la lista
        print("*" * 40)
        for i, libro in enumerate(biblioteca, 1):
            if len(libro['titulo']) > 31:
                titulo = libro['titulo'][:28]+ "..."
                print(f"* {i:<3}* {titulo:<31} *")
            else:
                titulo = libro['titulo']
                print(f"* {i:<3}* {titulo:<31} *")
        print("*" *30)
        input("Presione una tecla...")
        return        
    else:
        print ("No hay libros disponibles")
        

def buscar_libro():
    print("\n--- BUSCAR LIBRO ---")
    print("1. Buscar por título")
    print("2. Buscar por autor")
    
    opcion = input("Selecciona una opción (1-2): ")
    termino_busqueda = input("Ingresa el término de búsqueda: ").lower()
    
    resultados = []
    
    for libro in biblioteca:
        if opcion == "1" and termino_busqueda in libro['titulo'].lower():
            resultados.append(libro)
        elif opcion == "2" and termino_busqueda in libro['autor'].lower():
            resultados.append(libro)
    
    if resultados:
        print(f"\n--- RESULTADOS DE BÚSQUEDA ({len(resultados)} encontrados) ---")
        for i, libro in enumerate(resultados, 1):
            estado = "Disponible" if libro['disponible'] else "Prestado"
            print(f"{i}. Título: {libro['titulo']}")
            print(f"   Autor: {libro['autor']}")
            print(f"   Año: {libro['año']}")
            print(f"   Estado: {estado}")
            print("-" * 30)
    else:
        print("No se encontraron libros")

#Prestar Libros
def prestamos():
    borrar_pantalla()
    #Verificar si hay libros
    if not biblioteca:
        print("No hay libros disponibles aun.")
        return
    else:
        #Pedir titulo
        termino = input(" ingrese el nombre del libro o autor").lower()
        # Crear una lista para guardar los libros encontrados
        libros_encontrados=[]

        #Hacemos la busqueda y en caso de encontrar lo agregamos a la lista
        for libros in biblioteca:
            if termino in libros['titulo'].lower() or termino in libros['autor'].lower():
                libros_encontrados.append(libro)

        #Si no encontro nada:
        if not libros_encontrados():
            print("No se encontro ningun libro") 
            return
        
        #Mostrar resultados:
        print("***** RESULDADOS")
        for i, libros in enumerate(libros_encontrados, 1):
            if len(libros['titulo']) > 31:
                titulo = libros['titulo'][:28]+ "..."
                print(f"* {i:<3}* {titulo:<31} *")
            else:
                titulo = libros['titulo']
                print(f"* {i:<3}* {titulo:<31} *")





#Menu principal

while True:
    borrar_pantalla()
    print("GESTION DE BIBLIOTECA ")
    print("*" *20)
    print("1- Agregar libros NUEVOS")
    print("2- Mostrar los libros")
    print("3- Buscar un libro")
    print("4- Prestar un libro")
    print("5- Devolver un libro")
    print("6- Eliminar un libro")
    print("7- Salir")

    try: 
        print("*" *20)
        opcion = int(input("Opcion: "))
    except ValueError:
        print("*" *20)
        print(" Opcion invalida")
        input("Presione una tecla...")
        continue
    if opcion == 1:
        agregar()
        input("presione una tecla...")
    elif opcion == 2:
        mostrar_biblioteca()
        input("presione una tecla...")

    elif opcion == 3:
        buscar_libro()
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

