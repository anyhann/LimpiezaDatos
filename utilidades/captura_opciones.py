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

def leer_opciones_pantalla(opciones: dict) -> str:
    """
    Función que imprime pares clave-valor de un diccionario para dar la opción
    al usuario de elegir algo.
    Devuelve la clave elegida en formato string.
    """
    claves = opciones.keys()
    opciones_str = "\n".join(["Introduzca {}: {}".format(clave, opciones[clave]) for clave in claves])
    while True:
        print(opciones_str + "\n")
        opcion = input("Ingrese una opción (o bien q para salir): ")
        if opcion in claves:
            print("Opción seleccionada:", opciones[opcion])
            return opcion
        elif opcion == "q":
            print("Adiós")
            break
        else:
            print("Opción inválida. Intente nuevamente o pulse q para salir.")     
if __name__ == "__main__":
    opcion_seleccionada = leer_opciones_pantalla({"1": "Haz esto", "2": "Haz lo otro", "3": "Haz lo de más allá", "q": "Salir"})
    print("La opción seleccionada fue:", opcion_seleccionada)
