import os

# === 1. Configuración de rutas ===
directorio_actual = os.path.dirname(__file__)
nombre_carpeta = "ejercicio6"  # ← ✅ Nombre corregido
ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

# Crear la carpeta si no existe
os.makedirs(ruta_carpeta, exist_ok=True)

# === 2. Cargar productos desde la carpeta ===
productos = {}
ruta_datos = os.path.join(ruta_carpeta, "supermercado.dat")

if not os.path.exists(ruta_datos):
    print(f"⚠️ Advertencia: '{ruta_datos}' no existe. Se creará al salir.")
else:
    with open(ruta_datos, "r", encoding="utf-8") as base:
        for linea in base:
            linea = linea.strip()
            if linea:
                partes = linea.split()
                if len(partes) < 3:
                    continue
                nombre = ' '.join(partes[:-2])
                precio = float(partes[-2])
                cantidad = int(partes[-1])
                productos[nombre] = {'precio': precio, 'cantidad': cantidad}

# === 3. Funciones ===
pedido = {}

def ver_productos():
    if not productos:
        print("No hay productos cargados.")
        return
    for num, (produc, datos) in enumerate(productos.items(), 1):
        print(f"{num}. {produc:30} - ${datos['precio']:.2f} - {datos['cantidad']} unidades")

def compra():
    while True:
        print("\nIngresar Producto")
        articulo = input("Artículo: ").strip()
        if not articulo:
            continue
        try:
            art_cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")
            continue

        if articulo in productos:
            if productos[articulo]['cantidad'] >= art_cantidad:
                productos[articulo]['cantidad'] -= art_cantidad
                pedido[articulo] = art_cantidad
                print(f"✅ Agregado: {art_cantidad} de {articulo}")
            else:
                print(f"❌ Stock insuficiente. Solo hay {productos[articulo]['cantidad']} unidades.")
        else:
            print(f"🔍 Artículo '{articulo}' no encontrado.")

        if input("\n¿Agregar otro artículo? (s/n): ").lower() != "s":
            break

def generar_ticket():
    if not pedido:
        print("No hay productos en el pedido aún.")
        return

    total = 0
    ruta_ticket = os.path.join(ruta_carpeta, "Ejercicio6-ticket.md")

    with open(ruta_ticket, "w", encoding="utf-8") as arch:
        arch.write("#" * 40 + "\n")
        arch.write("#          TICKET DE COMPRA           #\n")
        arch.write("#" * 40 + "\n\n")
        for articulo, cantidad in pedido.items():
            precio = productos[articulo]['precio']
            subtotal = precio * cantidad
            total += subtotal
            arch.write(f"{articulo:>25} x{cantidad:2}  ${subtotal:6.2f}\n")
        arch.write("\n" + "-" * 40 + "\n")
        arch.write(f"{'TOTAL':>30} ${total:6.2f}\n")
        arch.write("-" * 40 + "\n")

    print(f"✅ Ticket guardado en: {ruta_ticket}")

# === 4. Menú principal ===
while True:
    print("\n=== MENÚ ===")
    print("1- Ver productos")
    print("2- Hacer un pedido")
    print("3- Generar ticket")
    print("4- Salir")
    opcion = input("Opción: ")

    if opcion == '1':
        ver_productos()
    elif opcion == '2':
        compra()
    elif opcion == '3':
        generar_ticket()
    elif opcion == '4':
        with open(ruta_datos, "w", encoding="utf-8") as base:
            for nombre, datos in productos.items():
                base.write(f"{nombre} {datos['precio']} {datos['cantidad']}\n")
        print("✅ Datos guardados. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")