
#######################################################################
#                  PREPARAMOS EN ENTORNO
#######################################################################
import os
import random #<------ libreria ramdon

# 1. Definir dónde está mi script
directorio_actual = os.path.dirname(__file__)

# 2. Definir el nombre de la carpeta que quiero crear
nombre_carpeta = "Datos"

# 3. Crear la ruta completa de la carpeta
ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

# 4. Crear la carpeta si no existe
os.makedirs(ruta_carpeta, exist_ok=True)

# 5. Creamos 2 archivos para tener la informacion separada
ruta_agenda = os.path.join(ruta_carpeta, "preguntas.txt")

########################################################################
#                   FUNCIONES                                          #
########################################################################

#------------------BORRAR PANTALLA-------------------
def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#-----------------CARGAR AGENDA ---------------------
def cargar_agenda(agenda):
    try:
        with open(ruta_agenda, 'r', encoding="utf-8") as archivo:
            if archivo:
                for linea in archivo:
                    partes = linea.strip().split("#")
                    datos = {'nombre': partes[0],
                             'telefono': partes[1],
                             'correo': partes[3]}
                    #Agregamos el diccionario a la lista con append
                    agenda.append(datos)
                print("Carga exitosa")
    
    except FileExistsError:
        with open(ruta_agenda, 'w', encoding="utf-8") as archivo:
            pass

#----------------- AGREGAR CONTACTO---------------------
def agregar_contacto(agenda):
    #Cargar datos
    nombre= input("* Nombre: ")
    try:
        telefono = int(input("* Telefono: "))
        correo = input("* Correo: ")
        datos = {'nombre': nombre,
                 'telefono': telefono,
                 'correo': correo}
                #Agregamos el diccionario a la lista con append
        agenda.append(datos)

    except ValueError:
        print("DATO MAL INGRESADO")



#-------------------VER CONTACTOS -----------------------
def ver_contactos(agenda):
    for num, linea in enumerate(agenda, 1):
        print (f"{num} - {linea['nombre']} - Tel: {linea['telefono']} - Correo: {linea['correo']}\n")
    

#---------------------GUARDAR DATOS ----------------------
'''def guardar():
    with open(ruta_agenda, 'w', encoding="UTF-8")'''

