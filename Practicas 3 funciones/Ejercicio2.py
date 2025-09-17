# Ejercicio 2: Calculadora simple con funciones 

#Crea funciones para suma, resta, multiplicación y división. 

#calculadora en python

#crear un menu, 
#elwgie l funcion que quiero utilizr.
#Volver al menu

def menu ():
    while True:
    
        print("**********************")
        print("*.   CALCULADORA.    *")
        print("**********************")
        print("*  Elija una opción: *")
        print(" 1) ---> Suma.")
        print(" 2) ---> Resta") 
        print(" 3) ---> Multiplicación")
        print(" 4) ---> División")
        print("***********************")
        try:
            eleccion = int(input("OPCIÓN:"))
            print("***********************")
            if 0< eleccion <5:
                return eleccion
            else:
                print("Numero incorrecto. Intente nuevamente")
        except ValueError:
            print("Dato invalido, intente nuevamente")
        
def entrada ():
    try:
        num1 = float(input("primer numero: "))
        num2 = float(input("segundo numero: "))
        
        return num1, num2
    except ValueError:
        print ("Dato incorrecto")
        
        
       
        
def suma(): 
    a,b = entrada()
    print(f"La suma de {a} + {b} es: ", a+b)
    
def resta():
    a,b = entrada()
    print(f"La resta de {a} - {b} es: ", a-b)
    
def division():
    a,b = entrada()
    if a == 0 or b==0:
        print("No se puede dividor un cero!")
    else:
        print(f"La división de {a} / {b} es: ", a/b)
    
def multiplicacion():
    a,b = entrada()
    print(f"La multiplicación de  {a} x {b} es: ", a*b) 
   
   
        
opcion = menu()

#Validar opcion

if opcion == 1:
    suma()
elif opcion == 2:
    resta()
elif opcion == 3:
    multiplicacion()
elif opcion == 4:
    division()