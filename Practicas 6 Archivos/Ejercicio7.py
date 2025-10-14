
#######################################################################
import os

# 1. Definir dónde está mi script
directorio_actual = os.path.dirname(__file__)

# 2. Definir el nombre de la carpeta que quiero crear
nombre_carpeta = "ejericio7"

# 3. Crear la ruta completa de la carpeta
ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

# 4. Crear la carpeta si no existe
os.makedirs(ruta_carpeta, exist_ok=True)

# 5. Ahora sí, crear el archivo DENTRO de esa carpeta
ruta_archivo = os.path.join(ruta_carpeta, "datos.txt")

with open(ruta_archivo, "w") as arch:
    arch.write("Este archivo está en una carpeta que yo creé.\n")
    arch.write("¡Qué poder!")

print(f"✅ Archivo guardado en: {ruta_archivo}")
###############################################################################