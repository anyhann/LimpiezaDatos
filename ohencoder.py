import numpy as np
import pandas as pd
import os
from carga_datos import cargador


def crea_dummies(df, columnas):
    """columnas = df.columns.tolist()"""
    
    for col in columnas:
        df = pd.concat([df, pd.get_dummies(df[col], prefix=col, prefix_sep='_',)], axis=1)
        df = df.drop(col, axis=1)
        print(df)
    return df



def main():
    # Cargar un DataFrame de ejemplo
    main_file_path = os.path.abspath(__file__)
    data = cargador(os.path.join(os.path.dirname(main_file_path), "categorias de corredores.csv"))
    # Obtener la lista de columnas del DataFrame
    columnas = data.columns.tolist()

    # Presentar las columnas con un número asignado
    for i, col in enumerate(columnas, 1):
        print(f"{i}. {col}")

    # Pedir al usuario que elija las columnas por teclado
    seleccion = input("Elige las columnas (separadas por comas): ")
    indices_seleccionados = [int(index) - 1 for index in seleccion.split(",")]

    # Obtener las columnas seleccionadas
    columnas_seleccionadas = [columnas[idx] for idx in indices_seleccionados]

    # Llamar a la función crea_dummies
    df_dummies = crea_dummies(data, columnas_seleccionadas)
    

    # Imprimir el DataFrame resultante
    print(df_dummies.columns.T)

if __name__ == '__main__':
    main()