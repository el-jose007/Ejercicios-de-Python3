# validar contraseñas correo y contraseña. 
#debe tener @, 8 caracteres, una mayoscula y un numero. 
#El correo debe tener un @ y no debe empezar ni con un
#ni punto.  por ultimo debe
# terminar con .com

#dividimos en tres modulos la solución:
#1) pedir los datos. 
#2) validar correo
#3) validar contraseña 

#funcion validar correo:
def correo(dato):
    if len(dato) < 8:
        return False
    if "@" not in dato: 
        return False
    if dato[0] in ["@","."]:
        return False
    if not dato.endswith(".com"):
        return False
    else:
        return True
        
    
def contrasenia(dato):
    if len(dato)<8:
        return False
    mayus = any(c.isupper() for c in dato)
    num = any(c.isdigit() for c in dato)
    
    #validamos
    if mayus and num:
        return True
    else:
        return False    
        
        
    
#pedir datos
mail = input("ingresar correo:  ")
mailtrue = correo(mail)



if mailtrue == True:
    print(f"correo: {mailtrue}")
    passw = input("Ingresar contraseña:  ")
    passtrue = contrasenia(passw)
    if passtrue:
        print("Pass correcto")
    else:
        print("pass incorrecto")   
else: 
    print ("correo invalido")
        