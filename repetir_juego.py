def preguntar_repetir():
    while True:
        opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()

        if opcion == "s":
            return True
        elif opcion == "n":
            return False
        else:
            print("Opción inválida.\n")
