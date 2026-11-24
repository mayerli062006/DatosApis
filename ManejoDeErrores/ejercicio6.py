while True:
    try:
        numero = int(input("Escribe un numero: "))
        break
    except ValueError:
        print("Eso no es un numero entero. Intenta de nuevo.")
        
        
        

print("Recibi el numero valido:", numero)
