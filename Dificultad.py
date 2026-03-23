def elegir_dificultad():
    print("Selecciona la dificultad:")
    print("1. Fácil (1-10)")
    print("2. Medio (1-20)")
    print("3. Difícil (1-50)")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        return 1, 10
    elif opcion == "2":
        return 1, 20
    elif opcion == "3":
        return 1, 50
    else:
        print("Opción inválida, se usará dificultad media.")
        return 1, 20
