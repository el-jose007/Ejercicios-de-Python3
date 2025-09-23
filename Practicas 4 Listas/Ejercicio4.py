#pide nombres indefinidamente y los agrega a una lista. no 
#permite agregar duplicados. después, al poner fin corta y presenta
#la lista ordenada alfabeticamente y luego en sentido contrario. 

lista=[]
print("ingresa nombres. envia 'fin' para parar")
while True:
    nombre = input("-->").lower()
    if nombre not in lista and nombre != "fin": 
        lista.append(nombre)
    elif nombre == "fin":
        break
    else: 
        print(" Repetido, coloca otro")

ordenada = sorted(lista)
al_reves = list(reversed(ordenada))
print(" ")
print("ordenada")
print("**********************")
for palabra in ordenada:
    print(palabra)

print(" ")
print("Al revés")
print("**********************")
for palabra in al_reves:
    print(palabra)
        
        
        