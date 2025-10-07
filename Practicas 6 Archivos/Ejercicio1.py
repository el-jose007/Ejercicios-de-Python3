#Crear un archivo y leerlo
import os

# Obtiene la carpeta donde está este archivo .py
directorio_actual = os.path.dirname(__file__)

# Crea la ruta completa al nuevo archivo
ruta_archivo = os.path.join(directorio_actual, "mi_archivo.txt")

# Escribe en esa ubicación
with open(ruta_archivo, "w") as arch:
    arch.write("Hola, este archivo está en la misma carpeta que el código.")