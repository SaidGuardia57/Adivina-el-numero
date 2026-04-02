#intentos.py

def manejar_intentos(numero_secreto, minimo, maximo):
    intentos = 5

    while intentos > 0:
        try:
            numero = int(input(f"Adivina el número ({minimo}-{maximo}): "))
        except:
            print("Ingresa un número válido.\n")
            continue 
 
        if numero == numero_secreto:
            print("¡Correcto! Adivinaste el número ")
            return True

        elif numero < numero_secreto:
            print("El número secreto es MAYOR\n")
        else:
            print("El número secreto es MENOR\n")

        intentos -= 1
        print(f"Te quedan {intentos} intentos\n")

    print(f" Upss Perdiste, El número era {numero_secreto}\n")
    return False
