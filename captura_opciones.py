def leer_opciones_teclado():
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            # Hacer algo para la opción 1
            print("Opción 1 seleccionada")
            return opcion
        elif opcion == "2":
            # Hacer algo para la opción 2
            print("Opción 2 seleccionada")
            return opcion
        elif opcion == "3":
            # Hacer algo para la opción 3
            print("Opción 3 seleccionada")
            return opcion
        elif opcion == "q":
            # Salir del ciclo y devolver la opción seleccionada
            return "Ninguna"
        else:
            print("Opción inválida. Intente nuevamente.")


  

opcion_seleccionada = leer_opciones_teclado()
print("La opción seleccionada fue:", opcion_seleccionada)
