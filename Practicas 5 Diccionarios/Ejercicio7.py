#Encontrar el producto mas caro

productos = {
    "pan" : 3000,
    "tarta" : 6000,
    "cuernitos" : 2000,
    "tortas" : 8000
}

mayor = max(productos, key=productos.get) #analiza los datos y toma el nombre del que tenga valor mas alto
print(f"el producto mas alto es {mayor} y cuesta ${productos[mayor]}")

''' Aca primero encontramos el nombre del mas caro y luego
imprmimos el nombre del diccionario con el nombre de la clave, lo que devuelve el valor'''


