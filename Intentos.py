#intentos.py

def manejar_intentos(numero_secreto, minimo, maximo):
    intentos = 5

while intentos > 0:
    numero = int(input("Adivina el número: "))
    intentos -= 1

    print(f" Upss Perdiste, El número era {numero_secreto}\n")
    return False
# Versión final de Maria