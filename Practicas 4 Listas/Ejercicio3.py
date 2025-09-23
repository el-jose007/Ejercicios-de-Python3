#crear una lista de nombres y buscar
# si no esta en la lista. devolver el puesto

lista =["mario", "lidia", "hilda", "diego", "mariana", "soledad","juana","yanel","nancy", "jose", "mauro"]

nombre = input("Elige un nombre de la cuadra: ").lower()
no = True
for i in range(len(lista)):
    if lista[i] == nombre:
        print(f"{nombre} esta en la posición {i+1}")
        no = False
        break

if no:
    print ("no esta")
