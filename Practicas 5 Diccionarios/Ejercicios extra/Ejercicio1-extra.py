#Crear un diccionario con los datos d un usuario

perfil = {
    'nombre' : 'jose',
    'Apellido':'dominguez',
    'telefono':'1168155821'  

}

for clave, valor in perfil.items():
    print(f"{clave.capitalize()}: {valor}")
