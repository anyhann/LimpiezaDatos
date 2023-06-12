from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd
from captura_opciones import leer_opciones_pantalla


def normalizador(datos):
    
    # Obtener solo las columnas numéricas
    datos = datos.select_dtypes(include=['int64', 'float64'])
    """
    Normaliza los datos preguntando por el algoritmo de normalización más conveniente
    """
    print("""Normalizadores disponibles:""")
    opciones = {"1": "min-max scaler",
        "2": "Standard scaler",
        "3": "max- abs scaler",
        "q": "Salir"}
    eleccion = leer_opciones_pantalla(opciones)
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
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "Corredores Latinos con Categorías.csv"))
    print(normalizador(datos))