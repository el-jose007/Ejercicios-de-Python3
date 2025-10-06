''' Ejercicio 4: Mini traductor español-inglés 

Situación:
Estás aprendiendo inglés y quieres un programa que te ayude a traducir palabras básicas. 

Objetivo:
Crear un diccionario de traducciones y permitir al usuario buscar una palabra. 

Instrucciones:   

    Crea un diccionario con al menos 5 palabras en español como claves y su traducción como valor.  
    Pide al usuario una palabra.  
    Si está en el diccionario, muestra la traducción.  
    Si no, avísale que no está registrada.
     '''

diccionario ={
    'hello' : 'hola',
    'while': 'mientras',
    'where' : 'donde',
    'sun' : 'sol,',
    'moon': 'luna'
}

#Ingresar la palabra
palabra = input("Ingrese la palabra a buscar: ")

# buscar si esta la clave.
if palabra in diccionario:
    print (f"la traduccion de {palabra} es {diccionario[palabra]}")
else:
    print("No esta la palabra en el diccionario")


