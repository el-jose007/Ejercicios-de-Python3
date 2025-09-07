#Pide edad y país. En EE.UU. se vota a los 18, en Brasil a los 16, 
# en Arabia Saudita... ni lo preguntes.

#Pedir datos
try:
    edad = int(input("ingrese su edad"))
    if edad >0 and edad < 130:
        pais = input("Ingrse su Pais (EEUU o Americano, Brazil o brasilero o Arabia o saudi: ")
        if pais == "EEUU" or pais == "eeuu" or pais == "Eeuu" or pais == "Americano":
            if edad >=18:
                print(f"con {edad} años, estas Apto para votar")
            else:
                print("Eres menor, y no puedes votar el Estados unidos")
        elif pais == "brasil" or pais == "Brasil" or pais == "BRASIL" or pais=="brasilero":
            if edad >= 16:
                print(f"Con {edad} estas apto para votar en Brasil")
            else:
                print("eres menor y no puedes votar.")
        elif pais =="Arabe" or pais == "ARABE" or pais =="arabe" or pais == "saudi":
            print("aqui ni votas, tienes una monarquia")

    else:
        print("tu dato no sirve para este programa.")
except ValueError:
   print("El dato ingresado es un error") 

#catalogarlos