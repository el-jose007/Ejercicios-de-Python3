# Registro de usuarios con funciones. nombre, apellido, dni. 


def validar_nombre(nombre):
    return nombre.isalpha()

def validar_apellido(apellido):
    return apellido.isalpha()
def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8


#ingresar datos:
nombre = input("Nombre: ")
apellido = input("Apellido: ")
dni = input("Dni: ")

if validar_nombre(nombre) and validar_apellido(apellido) and validar_dni(dni):
    print("Datos correctos")
