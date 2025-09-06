'''Ejercicio 10: Simulador de cajero automático (versión simple)
Saldo inicial = 1000. Permite:
1-er saldo
2-Retirar dinero
3-Depositar
4-Salir
Con operaiones infinitas'''

#Establecer saldo inicial.
saldo = 1000
print ("Bienveniso al Cajero automatico. Elija una opcion")
clave = "1234"
intentos = 3
ingreso = False

#ingrese la clave
for i in range (3):
    print("Ingrese su clave:" )
    clave_ingresada = input("--> ")
    if intentos != 0:
        if clave_ingresada == clave:
            ingreso = True
            break
        else:
            intentos -= 1
            print("Error. Clave incorrecta. le quedan {intentos} intentos")
            
else:
    print("Intentos superados. Cerrando sesion")    

#Crear un menu
while ingreso == True:
    print(" Bienvenido")
    print("*******************")
    print("1 - Ver saldo")
    print("2 - Retirar Saldo")
    print("3 - Depositar")
    print("4 - Salir")

    opcion = input("--> ")

    if opcion == "1":
        print(f"su saldo es: ${saldo}")
    elif opcion == "2":
        try:
            print("Ingrese el Monto:")
            retirar = float(input("-->"))
            if saldo >= retirar:
                saldo -= retirar
                print(f"Su nuevo saldo es: ${saldo}")
            else:
                print("--> Saldo es insuficiente <--")
        except ValueError:
            print("ERROR")
            continue
    elif opcion == "3":
        print ("Depositar:")
        try:
            deposito = float(input("--> "))
            saldo += deposito
            print(f"Su nuevo saldo es: ${saldo}")
        except ValueError:
            print("ERROR.")
            continue
    elif opcion == "4":
        break
    else:
        print("ingrese una opcion valida")





