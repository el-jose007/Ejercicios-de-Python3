'''👉 Un nombre de usuario debe cumplir:

Tener entre 5 y 12 caracteres.

Solo puede contener letras, números y guion bajo (_).

Debe empezar con una letra.'''

user = input("Nombre de usuario: ")

# 1. Verificar cantidad de caracteres
if len(user) < 5 or len(user) > 12:
    print("Clave rechazada (debe tener entre 5 y 12 caracteres).")
else:
    # 2. Verificar que empiece con una letra
    if not user[0].isalpha():
        print("Clave rechazada (debe empezar con una letra).")
    else:
        # 3. Verificar que solo tenga letras, números o guion bajo
        valido = True
        for c in user:
            if not (c.isalnum() or c == "_"):
                valido = False
                break

        if valido:
            print("Clave aceptada")
        else:
            print("Clave rechazada (caracteres inválidos).")