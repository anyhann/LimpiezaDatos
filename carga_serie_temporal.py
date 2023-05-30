"""
Crear una funcion que coja una columna y la convierta en indice
"""
from carga_datos import cargador
from columna_DateTime import convertir_a_datetime
import os

def conversion_a_serie_temp(dataframe, columna):
    # Convertir la columna de texto a datetime
    dataframe[columna] = convertir_a_datetime(dataframe[columna])

    dataframe.set_index(columna, inplace=True)
    return dataframe


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))
    datos = conversion_a_serie_temp(datos, "Time")
    print(datos.index)
    formato = '%Y-%m-%dT%H:%M:%SZ'