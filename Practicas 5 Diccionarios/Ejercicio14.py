'''🔹 Ejercicio 5: Estudiante y sus notas 

Situación:
Eres profesor y quieres llevar un registro básico de un estudiante, incluyendo sus calificaciones. 

Objetivo:
Usar un diccionario que contenga nombre y lista de notas, y calcular el promedio. 

Instrucciones:   

    Crea un diccionario estudiante con claves: "nombre" y "notas" (una lista de números).  
    Calcula el promedio usando sum() y len().  
    Muestra el resultado con formato.
     '''

alumno ={
    'nombre' : 'juan perez',
    'notas' : [3,5,7,9,8,5,9]
}

promedio= sum(alumno['notas'])/ len(alumno['notas'])
print(f"El alumno {alumno['nombre']} tiene un promedio de {promedio:.2f}")
