
'''Ejercicio 10: **Sistema de inventario para una tienda**

**Situación:**  
Eres encargado de una tienda y necesitas un sistema simple para gestionar el stock de productos.

**Objetivo:**  
Crear un diccionario de inventario y permitir operaciones: ver, agregar, sacar.

**Instrucciones:**  
- Inicia con un diccionario inventario con algunos productos y cantidades.  
- Haz un menú con opciones: ver, agregar, sacar, salir.  
- Usa .get() para evitar errores si el producto no existe.  
- Valida que no saques más de lo disponible.
'''def ver():
    print("INVENTARIO:")
    for nombre, clave in inventario.items():
        print(f"{nombre} : {clave}")
    return 
    
def agregar():
    nombre = input("Agregar: ").lower()
    cantidad = int(input("Cantidad: "))
    
    inventario[nombre] = inventario.get(nombre, 0) + cantidad
    print("Cantidad agregada")
    
def sacar():
    nombre = input("Sacar: ").lower()
    stock = inventario.get(nombre, 0)

    if stock == 0: 
        print("⚠️ No hay ese producto")
        return 
    else:
        cantidad = int(input("Cantidad: "))
        if cantidad <= stock:
            inventario[nombre] = stock - cantidad
            print(f"✅ Listo, ahora hay {inventario[nombre]}")
        else:
            print("⚠️ No hay tantas unidades")    
        
    
inventario = {'manzana': 50, 'banana': 30, 'ciruela': 25}

while True:
    opcion = input("\nOpciones: ver | agregar | sacar | salir\n> ").lower()
        
    if opcion == 'salir':
        print("👋 Adiós")
        break 
    
    elif opcion == 'ver':
        ver()
        input("Presione una tecla para continuar...")
    elif opcion == 'agregar':
        agregar()
        input("Presione una tecla para continuar...")
    elif opcion == 'sacar':
        sacar()
        input("Presione una tecla para continuar...")
    else:
        print("⚠️ Opción equivocada")
