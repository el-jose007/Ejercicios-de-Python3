#mostrar productos con sus precios

productos = {
    "pan" : 3000,
    "tarta" : 6000,
    "cuernitos" : 2000
}

for cosas, precios in productos.items():
    print(f"Producto: {cosas} - Precio: ${precios}")

print(f"suman un total de ${sum(productos.values())}")