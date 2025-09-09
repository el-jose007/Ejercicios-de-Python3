'''Ejercicio 5: Simulador de contraseña segura 

Pide una contraseña y verifica si es "segura": 

    Al menos 8 caracteres
    Tiene al menos una letra minúscula
    Tiene al menos una letra mayúscula
    Tiene al menos un número
    No tiene espacios
     '''

while True:
    #Variables para usar de llave
    minus = False
    mayus = False
    numero = False
    espacios = False

    #ingresar el dato
    print("Ingresa tu contraseña: ")
    passw = input("--> ")

    # recorrer la cadena y verificar
    if len(passw) >=8:
        for caracter in passw:
            if caracter == " ":
                 espacios = True
            elif caracter.islower():
                minus = True
            elif caracter.isupper():
                    mayus = True
            elif caracter.isdigit():
                    numero = True
            
        #VERIFICACION FINAL y conteo de errores.
        
        if minus and mayus and numero and not espacios:
            print("<<<<<<  \u2705CLAVE ACEPTADA   >>>>>>")
            break
        else:
            print("No cumple con los siguientes parametros")
            if not minus:
                print("Falta Minusculas")
            if not mayus:
                print("Falta Mayusculas")
            if not numero:
                print("Falta un numero")
            if espacios: #se evalua como True. interesante!
                print("Contiene un espacio")
    else:
        print("Contraseña incorrecta. Debe tener 8 caracteres o mas.")


