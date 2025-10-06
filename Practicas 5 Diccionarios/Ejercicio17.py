'''
'''
estudiantes = [
    {'nombre':'joaquin', 'edad': '12', 'nacionalidad': 'argentino'},
    {'nombre': 'paula','edad':'39','nacionalidad':'argentina'},
    {'nombre': 'jose','edad': '38','nacionalidad':'argentina'}
    ]

#mostrar la lista.
for alumno in estudiantes:
    for clave, valor in alumno.items():
            print(f"{clave}: {valor}")
    print("*" *15)
            