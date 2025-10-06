'''Ejercicio 9: **Búsqueda de estudiante**

**Situación:**  
Un alumno quiere saber si está registrado en la base de datos.

**Objetivo:**  
Buscar un estudiante por nombre dentro de la lista de diccionarios.

**Instrucciones:**  
- Pide un nombre al usuario.  
- Recorre la lista `estudiantes`.  
- Si lo encuentras, muestra sus datos.  
- Si no, avisa que no está.
'''
estudiantes = [
    {'nombre':'carlos','apellido': 'tejedor'}
    ]
encontrado = False
#pedir nombre de usuario
nombre = input("--> ").lower()

#recorre la lista
for est in estudiantes:
    if est['nombre'].lower() == nombre:
        print(f"{est['nombre'].capitalize()}, {est['apellido'].capitalize()}")
        encontrado = True

if not encontrado:
    print("No encontrado")
    