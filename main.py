#main.py

from dificultad import elegir_dificultad
from numero_secreto import generar_numero
from intentos import manejar_intentos
from repetir_juego import preguntar_repetir
from mensajes import bienvenida


def main():
    bienvenida()

    while True:
        minimo, maximo = elegir_dificultad()
        numero_secreto = generar_numero(minimo, maximo)

        manejar_intentos(numero_secreto, minimo, maximo)

        if not preguntar_repetir():
            print("Gracias por jugar ")
            break


if __name__ == "__main__":
    main()
