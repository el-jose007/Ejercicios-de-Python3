#Crea una función que verifique si un email tiene @ y .com.

def comprobacion(mail):
    if "@" in mail:
        if mail.endswith(".com"):
            return True
        else:
            return False
    else:
        return False
    return True


mail= input("ingrese mail: ")
analisis = comprobacion(mail)
print(analisis)
