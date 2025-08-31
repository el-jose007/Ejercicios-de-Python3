#Mejoramos el ejercicio anterior.

try: 
    nota = float(input("Ingrese su nota: "))
    if nota >= 0 and nota<=100:

        if nota >90:
            print("Tenes una A!!!")
        elif nota >=80:
            print("Tenes una B, bien")
        elif nota >=70:
            print("Tenes una C: flojeli")
        elif nota >=60:
            print("Tienes una D, casi no pasas")
        elif nota < 60:
            print("Estas reproobado!!!")
    else:
        print("El numero que ingresaste no sirve")

except ValueError:
    print("Opcion incorrecta")