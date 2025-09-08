'''Ejercicio 5: Simulador de contraseña segura 

Pide una contraseña y verifica si es "segura": 

    Al menos 8 caracteres
    Tiene al menos una letra minúscula
    Tiene al menos una letra mayúscula
    Tiene al menos un número
    No tiene espacios
     '''
#Variables para usar de llave
canti_caracteres = False
minus = False
mayus = False
numero = False


while True:
    print("Ingresa tu contraseña: ")
    passw = input("--> ").split() # limpio de espacios
    # recorrer la cadena y verificar
    if len(canti_caracteres) >=8:
        for caracter in passw:
            if caracter.islower():
                minus = True
            elif caracter.isupper():
                mayus = True
            elif caracter.isdigit():
                numero = True
        else:
            print("No cumple con los siguientes parametros")
            if minus == False:
                print("Falta Minusculas")
            if mayus == False:
                print("Falta Mayusculas")
            if numero == False:
                print("Falta un numero")
    else:
        print("Contraseña incorrecta. Debe tener 8 caracteres o mas.")


