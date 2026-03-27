def elegir_dificultad():
    while True:
        print("Selecciona la dificultad:")
        print("1. Fácil (1-10)")
        print("2. Medio (1-20)")
        print("3. Difícil (1-50)")

        opcion = input("Elige una opción (1/2/3): ")

        if opcion == "1":
            print("Elegiste Fácil\n")
            return 1, 10
        elif opcion == "2":
            print("Elegiste Medio\n")
            return 1, 20
        elif opcion == "3":
            print("Elegiste Difícil\n")
            return 1, 50
        else:
            print("Opción inválida, intenta de nuevo.\n")
