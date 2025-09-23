'''
Ejercicio 1: Lista de compras simple
Crea una lista, agrega elementos y muéstralos.'''

#Crear una lista, agregar  elementos y mostrarlos. 
lista =[] #lista Vacia
cantidades = []
print("ingresar los datos de la lista, uno por uno.")
print("Presione T para salir.")


while True:
    producto = input("Producto: ")
    if producto  == "T" or producto == "t":
        break
    try:
        cantidad = int(input("Cantidad: ")) 
        lista.append(producto)
        cantidades.append(cantidad)
        print("-----------------------")
    except ValueError:
        print("Cantidad invalida")

print("lista de Compras:")
print("----------------------")
for i in range(len(lista)): #Len devuelve un numero y no puede ser usdo con un in.
    print(f"* {lista[i]} ---------> {cantidades[i]} Unidades")

