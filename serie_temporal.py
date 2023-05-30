"""
Crear una funcion que coja una columna y la convierta en indice
"""
from carga_datos import cargador
from columna_DateTime import convertir_a_datetime
import pandas as pd
import os

def conversion_a_serie_temp(dataframe, columna):
    # Obtener la columna de texto y el formato de fecha del usuario
    columna_a_indice = input("Introduce el nombre de la columna de tiempo: ")

    # Convertir la columna de texto a datetime
    columna_datetime = convertir_a_datetime(columna)

    dataframe.set_index(columna_datetime, inplace=True)


if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec.csv"))
    conversion_a_serie_temp(datos, "Time")