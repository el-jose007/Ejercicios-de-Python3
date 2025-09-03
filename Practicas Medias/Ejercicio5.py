# pide un numero y muestra su tabla:

#pedimos
Numero =int(input("que numero te gustaria saber la tabla? el "))

for i in range(1,11):
    resultado = i * Numero
    print(f"{Numero} X {i}  = {resultado}")

