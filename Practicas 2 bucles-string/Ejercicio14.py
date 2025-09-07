#Pide un mensaje y una cantidad. Cuenta atrás desde ese número y al final muestra el mensaje.

#Pidiendo mensaje y cantidad
mensaje = input("mensaje: ")
cantidad =int(input("Cantidad"))

# Ejecutar
for i in range(cantidad,0,-1):
    print(f"{i}!")

print(f"{mensaje}!!!!")
