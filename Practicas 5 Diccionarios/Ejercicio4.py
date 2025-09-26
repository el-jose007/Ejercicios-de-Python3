'''Haz un programa que almacene nombres de alumnos con su edad, y muestre el nombre del mayor.'''
alumnos = {
    "juan" : 18,
    "pedro" : 17,
    "ezequiel" : 16
}

mayor = max(alumnos, key=alumnos.get) 
print (mayor)