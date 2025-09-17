'''
👉 El usuario debe ingresar un PIN y se valida:

Exactamente 4 dígitos.

Todos deben ser números.

No puede contener secuencias simples como "1234" o "0000".'''

#razonamiento.
#debe tener una cantidad.
#debe saber de que tipo es.
#no debe contener una secuencia

#empezamos! 
while True:
    cantidad = False
    not_secuencia = False
    
    print("ingrese su codigo")
    try:
        codigo = input("---->")
        
        #validamos uno
        if len(codigo) == 4:
            cantidad= True
        
        #validamos que sean numedos
        tipo = codigo.isdigit()
        
        # vemos que no sea secuencia común. 
        secuencia = [ "1111", "2222", "3333", "0000", "1234"]
        
        if codigo not in secuencia: 
            not_secuencia = True
        
        if cantidad and tipo and not_secuencia:
            print("Código valido!")
            break 
        else:
            print ("Código  invalido. intente nuevamente")
    
    except ValueError:
        print("caracter inválido")
        continue
        