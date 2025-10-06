'''
🔹 Ejercicio 7: Contador de frecuencia de letras 

Situación:
Estás analizando un texto y quieres saber qué letras aparecen más veces (como en criptografía o análisis de lenguaje). 

Objetivo:
Contar cuántas veces aparece cada letra en una palabra o frase. 

Instrucciones:   

    Pide una palabra al usuario.  
    Usa un diccionario para ir contando cada letra.  
    Si la letra ya está, suma 1; si no, créala con valor 1.  
    Muestra el resultado.
     '''

palabra = input("Palabra")

analisis ={}

#recorrer la palabra
for letra in palabra:
    if letra in analisis:
        analisis[letra] += 1
    else:
        analisis[letra] = 1

print(analisis)