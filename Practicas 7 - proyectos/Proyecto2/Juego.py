'''🔹 Paso 1: Objetivo del programa
Un juego donde se hacen preguntas, el usuario responde, y se lleva puntaje.
Al final, se muestra el resultado y se guarda el mejor puntaje. '''

''' FUNCIONALIDADES
MOTRAR PREGUNTAS,
MOSTRAS RESULTADOS. 
VERIFICAR SI GANO
GUARDAR PUNTOS
PERGUNTTAR SI QUIERE VOLVER A JUGAR'''


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
ruta_preguntas = os.path.join(ruta_carpeta, "preguntas.txt")
ruta_puntos = os.path.join(ruta_carpeta, "puntajes.txt")
preguntas= {}
puntajes = []
########################################################################
#                   FUNCIONES                                          #
########################################################################

#------------------BORRAR PANTALLA-------------------
def borrar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#-----------------CARGAR PREGUNTAS ------------------
def cargar_datos(preguntas):
    #Abrir el archivo
    with open(ruta_preguntas,"r", encoding="utf-8") as datos_preguntas:
        # recorrerlo lina a linea
        num = 0 #<----- vamos a contar las preguntas
        for linea in datos_preguntas:
            num +=1
            # tomar una linea y dividirla en pregunta respuesta
            partes = linea.strip().split("?")
            pregunta = partes[0]+"?"
            #tomar la respuesta y dividirla en 3
            opciones = partes[1].split("#")
            #Cargarla en una lista de diccionarios.
            preguntas[num] = {
                'pregunta': pregunta,
                'opciones': opciones
                }
    

#------------------CARGAR PUNTAJES ------------------
def cargar_puntajes():
    puntajes=[]
    #El objetivo seria cargar una lista de los 5 mejores puestos que esten 
    #guardados en memoria
    try:
        with open(ruta_puntos, 'r', encoding="utf-8") as datos_puntos:
            for linea in datos_puntos:
                partes = linea.strip().split("|")
                puntajes.append({'nombre': partes[0], 'puntos': int(partes[1])})
    except FileExistsError:
        pass
    return puntajes      

#------------------ELEGIR PREGUNTAS------------------
def generar_preguntas(preguntas):
    #cargar pregunta.
    preguntas_elegidas =[]
    # Saber la cantidad de preguntas y elegir 20 numeros al azar.
    cant_preguntas = len(preguntas)
    for a in range(10):
        while True:
            sorteo = random.randint(1,cant_preguntas)
            if not sorteo in preguntas_elegidas:
                preguntas_elegidas.append(sorteo)
                break
            else:
                continue
    return preguntas_elegidas
    #fijarse si entan el la lista de hechas. si no esta elegirla y si esta elegir otra.
    

#-----------------GENERAR RESPUESTAS-----------------
#Mezcla las respuestas del diccionario y devuelve el nuevo orden
def opciones_respuestas(num_pregunta):
    #tomar el numero de respuesta. 
    ordenada = preguntas[num_pregunta]['opciones']
    desordenada = random.sample(ordenada, len(ordenada))
    return desordenada
    

#-----------------COMPROBAR RESPUESTA----------------
def comprobar_respuesta(preguntas,num,orden):
    opcion = input("la correcta es: ").lower()
    if opcion == 'a' and orden[0] == preguntas[num]['opciones'][0]:
        return True
    if opcion == 'b' and orden[1] == preguntas[num]['opciones'][0]:    
        return True
    if opcion == 'c' and orden[2] == preguntas[num]['opciones'][0]:
        return True
    else:
        return False
        
        
#-----------------GENERAR TRIVIA --------------------
def trivia():
    nombre = input("Ingrese su Nombre: ")
    puntaje_trivia =0
    #generar un bucle de 20 preguntas
    lista_preguntas = generar_preguntas(preguntas)
    
    for num in lista_preguntas:
        borrar_pantalla()
        print (f"*"*45)
        print(f"*"+ (" "*43))
        print(preguntas[num]['pregunta'])
        print(f"*"*45)
        orden = opciones_respuestas(num)
        #recorremos la lista y mostramos en el orden generado
        print(f"A. {orden[0]}")
        print(f"B. {orden[1]}")
        print(f"C. {orden[2]}")
        
        eleccion = comprobar_respuesta(preguntas,num,orden)
        if eleccion:
            print(".    ¡¡CORRECTO!!")
            input("Siguiente pregunta")
            puntaje_trivia +=1
            borrar_pantalla()
        else: 
            print("¡¡INCORRECTO!!  ") 
            if orden[0] == preguntas[num]['opciones'][0]:
                print("La correcta era la A")
                input("Siguiente pregunta")
            elif orden[1] == preguntas[num]['opciones'][0]:
                print("La correcta era la B")    
                input("Siguiente pregunta")
            elif orden[2] == preguntas[num]['opciones'][0]:
                print("La correcta era la C")
                input("Siguiente pregunta")
    
    print(f"PUNTOS ACUMULADOS: {puntaje_trivia}")
    tabla = guardar_puntaje(nombre, puntaje_trivia)
    input("Inserte una tecla para continuar")
    borrar_pantalla()
    mostrar_tabla()
    input("Inserte una tecla para continuar")
    
    
#--------------------GUARDAR PUNTAJES----------------    
def guardar_puntaje(nombre, puntos):
    puntajes = cargar_puntajes()
    #guardar punto
    puntajes.append({'nombre':nombre, 'puntos':puntos})
    #ordenar dejar los promeros 5
    ordenar = sorted(puntajes, key= lambda x: x['puntos'], reverse=True)
    # Copiar los primeros 5 valores
    tabla_nueva =ordenar[:5]
    #grabar en un archivo 
    with open(ruta_puntos, 'w', encoding="utf-8") as archivo:
        for linea in tabla_nueva:
            archivo.write(f"{linea['nombre']}|{linea['puntos']}\n")
    return tabla_nueva
   
    
#------------------MOSTRAR TABLA---------------------
def mostrar_tabla():
    tabla = cargar_puntajes() #volvemos a cargar porque no se si lo que esta en memoria es lo mismo que lo guardado
    borrar_pantalla()
    print(f"**************** TABLA DE PUNTAJES ****************")
    for linea in tabla:
        print(f"* {linea['nombre']} ---------- {linea['puntos']}")
    

#-----------------Menu ------------------------------
def menu():
    cargar_datos(preguntas)
    borrar_pantalla()
    puntajes = cargar_puntajes()
    print(f"📝 JUEGO DE PREGUNTAS Y RESPUESTAS!\n")

    while True:
 
        print("\n--- Menú ---")
        print("1. Ver puntajes")
        print("2. Jugar")
        print("3. Salir")
        try:
            opcion = input("Elige: ")
        except ValueError:
            print("Opcion incorreecta...")
            continue

        if opcion == "1":
            mostrar_tabla()
        elif opcion == "2":
            trivia()
        elif opcion == "3":
            break
        else:
            continue

#------------------- INICIAR --------------------------
menu()