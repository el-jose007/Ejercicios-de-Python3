#Generar un archivo la carpeta, luego realizar:


#agregmamos la libreria
import os

# Obtiene la carpeta donde está este archivo .py
directorio_actual = os.path.dirname(__file__)

# Crea la ruta completa al nuevo archivo
ruta_archivo = os.path.join(directorio_actual, "Ejercicio4.txt")

# Escribe en esa ubicación
with open(ruta_archivo, "w") as arch:
    arch.write("Hola, este archivo está en la misma carpeta que el código.\n")


#leer el contenido.
with open(ruta_archivo, "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    print("-" *40)
    print(ruta_archivo)
    print("-" *40)

#agregamos contenido sin borrar los datos anteriores

with open(ruta_archivo,"a") as archivo:
    archivo.write("Esta es una nueva linea debajo de la anterior")



