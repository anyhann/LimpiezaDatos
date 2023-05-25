from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd


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


def normalizador(datos):
    """
    Normaliza los datos preguntando por el algoritmo de normalización más conveniente
    """
    print("""Normalizadores disponibles:
    1. min-max scaler
    2. Standard scaler
    3. max- abs scaler
    q. Salir
    """)
    eleccion = leer_opciones_teclado()
    if eleccion == "1":
        scaler = MinMaxScaler()
    elif eleccion == "2":
        scaler = StandardScaler()
    elif eleccion == "3":
        scaler = MaxAbsScaler()
    else:
        print("Los datos no se han normalizado")
        return datos
    normalized_data_array = scaler.fit_transform(datos)
    normalized_data = pd.DataFrame(normalized_data_array, columns = datos.columns)
    return normalized_data

if __name__ == "__main__":
    import os
    from carga_datos import cargador
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "hormigon.csv"))
    print(normalizador(datos))