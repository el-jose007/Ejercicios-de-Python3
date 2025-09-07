"""Pide una nota (0-100) y muestra la calificación:

90-100 → A (Excelente)
80-89 → B (Bien)
70-79 → C (Aprobado, pero estudiaste el día antes)
60-69 → D (Casi mueres, pero pasaste)
<60 → F (Te vieron en clase?)"""

#ingresar las Notas:
try: 
    nota = float(input("Ingrese su nota: "))

    if nota <= 100 and nota >89:
        print("Tenes una A!!!")
    elif nota <=89 and nota>79:
        print("Tenes una B, bien")
    elif nota <=79 and nota>69:
        print("Tenes una C: flojeli")
    elif nota <= 69 and nota >59:
        print("Tienes una D, casi no pasas")
    elif nota <= 59:
        print("Estas reproobado!!!")
    

except ValueError:
    print("Opcion incorrecta")
