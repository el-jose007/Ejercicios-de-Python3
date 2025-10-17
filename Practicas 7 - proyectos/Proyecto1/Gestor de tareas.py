'''🏁 Proyecto 1: Gestor de Tareas Personal
"El primer paso del organizado." 

🎯 Objetivo
Crear un programa que permita:

Agregar tareas
Ver todas las tareas
Marcar tareas como completadas
Eliminar tareas
Guardar todo en un archivo para que no se pierda
🧱 Estructura del Proyecto
Vamos a dividirlo en funciones:

cargar_tareas() → lee del archivo
guardar_tareas(tareas) → guarda en el archivo
mostrar_tareas(tareas) → muestra bonito
agregar_tarea(tareas) → pide y agrega
marcar_completada(tareas) → cambia estado
eliminar_tarea(tareas) → borra una
Menú principal → elige acción
Y usaremos una lista de diccionarios así:

tareas = [
    {"descripcion": "Estudiar Python", "completada": False},
    {"descripcion": "Hacer ejercicio", "completada": True}
]

💾 Formato del archivo: tareas.txt
Guardaremos cada tarea así:


Estudiar Python|False
Hacer ejercicio|True
→ Usamos | para separar descripción y estado.'''


#######################################################################
#                  PREPARAMOS EN ENTORNO
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
ruta_archivo = os.path.join(ruta_carpeta, "tareas.dat")


########################################################################
#                   FUNCIONES                                          #
########################################################################

#------------------BORRAR PANTALLA-------------------
def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return


#------------------CARGAR TAREAS----------------------

def cargar():
    tareas = []
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as datos_agenda:
            #Recoremos el archivo linea a linea, separandolo con strip
            for linea in datos_agenda: #recooro lina por linea
                partes = linea.strip().split("|")#limpia y divide
                #agrega el diccionario a la lista
                completada = partes[1] == "True"
                tareas.append({'descripcion': partes[0], 'completada': completada})
        return tareas


    except FileNotFoundError:
        #Si no existe el archivo lo vamos a crear
        with open(ruta_archivo, 'w', encoding="utf-8") as datos_agenda:
            pass
        print("Archivo Agenda.dat CREADO.")
        input("presione cualquier tecla... ")

        return tareas


#------------- GUARDAR TAREAS-------------------------
def guardar_tareas(tareas):
    #Abrir el archivo en formato write. 
    borrar_pantalla()
    with open(ruta_archivo, 'w', encoding="utf-8")  as datos_agenda:
        #recorrer la lista e ir pegandola 
        for item in tareas:#
            descrip = item["descripcion"]
            estado = item["completada"]
            datos_agenda.write(f"{descrip}|{estado}\n")
        print("guardado exitoso.")


#--------------MOSTRAR TAREAS-------------------------
def mostrar_tareas(tareas):
    if tareas:
        borrar_pantalla()
        print("*" * 45)
        print("           TAREAS ASIGNADAS           ")
        print("*" * 45)
        for num, tarea in enumerate(tareas, 1):
            estado = "Completa" if tarea["completada"] else "incompleta"
            print(f"{num:<3} | {tarea['descripcion']:<25} | {estado:^10}")
    else:
        print("Aun no hay tareas asignadas")


#---------------AGREGAR TAREA -------------------------
def agregar_tarea(tareas):
    borrar_pantalla()
    print("*" * 45)
    print("           AGREGAR TAREAS           ")
    print("*" * 45)
    #pedir la tarea, si la acaba de ingresar es que esta incompleta
    nueva_tarea = input("Ingresa la tarea: ").strip()
    if nueva_tarea:
        tareas.append({
            'descripcion': nueva_tarea, 
            'completada' : False
        })
        print("TAREA INGRESADA")
    else:
        print("No se puede ingresar una tarea en blanco")


#-------------- MARCA COMO COMPLETADA UNA TAREA -------
def marcar_completada(tareas):
    # mostramos la lista de tareas y le pedimos al usuario que diga que numero va a modificar
    if tareas:
        borrar_pantalla()
        mostrar_tareas(tareas)
        print("*" * 45)
        try:
            numero = int(input("Inrgese el numero de tarea que va a completar: "))-1
        except ValueError:
            print("ha ingresado un caracter invalido")
            return
        if 0 <= numero < len(tareas):
            #preguntarse si ese numero de tarea ya esta completado
            if not tareas[numero]['completada']:
                tareas[numero]['completada'] = True
                print("La tarea ha sido completada")
                return
            else:
                print("La tarea ya estaba completa")
                return
            

#-------------- ELIMINAR UNA TAREA-----------------------
def eliminar_tarea(tareas):
    if tareas:
        borrar_pantalla()
        mostrar_tareas(tareas)
        try:
            numero = int(input("Numero de tarea por eliminar: ")) - 1
        except ValueError:
            print(" Valor invalido.")
            return
        
        #Verificar que el valor sea adecuado
        if 0 <= numero < len(tareas):
            eliminado = tareas.pop(numero)
            print(f"El elemento {eliminado['descripcion']} ha sido eliminado")
            return
        else:
            print(f"El numero{numero + 1} no es valido. ")
            return
    else:
        print("Todavia no hay ninguna tarea, por favor ingresar una tarea")
        return


#----------------MENU PRINCIPAL---------------------------
def menu():
    tareas = cargar()
    borrar_pantalla()
    print("📝 Bienvenido a tu Gestor de Tareas")

    while True:
 
        print("\n--- Menú ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige: ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print("✅ Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Elige del 1 al 5.")


#------------iniciar programa-----------------------------
menu()
