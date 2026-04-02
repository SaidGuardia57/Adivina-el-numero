#main.py

from Dificultad import elegir_dificultad
from numero_secreto import generar_numero
from Intentos import manejar_intentos
from repetir_juego import preguntar_repetir
from mensaje import bienvenida


def jugar():
    minimo, maximo = elegir_dificultad()
    numero_secreto = generar_numero(minimo, maximo)

    manejar_intentos(numero_secreto, minimo, maximo)


def main():
    bienvenida()
    print("\n--- Bienvenido al juego de adivinar el número ---\n")

    while True:
        jugar()

        if not preguntar_repetir():
            print("Gracias por jugar 👋")
            break
        else:
            print("\n--- Nuevo juego ---\n")


if __name__ == "__main__":
    main()