''' Ejercicio 3: Modificar y verificar 

Agrega una clave y verifica si existe. '''

perfil = {
    'nombre':'jorge',
    'apellido':'gonzalez',
    'telefono': '1168155821'
}

#Agregar clave:
mail = input("ingrese su mail: ")
perfil['email'] = mail

for clave in perfil.keys():
    if clave == 'email':
        print(f"se creo bien la clave {clave}")
        
