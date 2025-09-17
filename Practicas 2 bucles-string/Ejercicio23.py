'''👉 Pide un correo y verifica:

Debe tener al menos un "@".

Debe tener al menos un "." después del "@".

No debe empezar ni terminar con "@" o ".".

No debe contener espacios.'''

# pedir correo

correo = input("ingrese el correo: ")

#Con mucho Python. para no anidar, voy a usar valiables y booleanos
asterisco = False
post_asterisco = False
espacios = False
terminacion = False


#Tiene asterisco?
if "@" in correo:
    posicion = correo.index("@")
    asterisco = True

    if "." in correo[posicion+1: ]:
        post_asterisco = True

terminacion = not (correo.startswith(".") or correo.startswith("@") or correo.endswith(".") or correo.endswith("@"))
if " " not in correo: 
        espacios = True


#Validar:
if asterisco and post_asterisco and terminacion and espacios:
    print("Correo Valido")
else:
    print("Correo invalido por")
    if not asterisco:
        print (" no tiene un arroba")
    if not post_asterisco:
        print("Le falta el punto despues del arroba")
    if not terminacion:
        print("Contiene al inicio o al final un caracter invalido")
    if not espacios:
        print("Contiene espacios")
        







