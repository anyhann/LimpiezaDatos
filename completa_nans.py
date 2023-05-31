from Serie_temporal import SerieTemporal
from carga_datos import cargador
import os
import pandas as pd



def detecta_nans(dataframe, columna):
    nulos = dataframe[columna].isnull()
    return nulos


def rellena_aislados(dataframe, columna):
    """
    Rellena valores nulos aislados, es decir, que tengan valor no nulo antes y después
    """
    filled_column = dataframe[columna].copy()
    # Si el primer valor es nulo, toma el segundo
    if pd.isnull(filled_column[0]) and len(filled_column) > 1:
        filled_column[0] = filled_column[1]
    # Si el último valor es nulo toma el penúltimo
    if pd.isnull(filled_column[-1]) and len(filled_column) > 1:
        filled_column[-1] = filled_column[-2]
    # En los nulos intermedios hace la media
    for i in range(1, len(filled_column) - 1):
        if pd.isnull(filled_column[i]):
            upper_value = filled_column[i - 1]
            lower_value = filled_column[i + 1]
            if pd.notnull(upper_value) and pd.notnull(lower_value):
                filled_column[i] = (upper_value + lower_value) / 2
    dataframe[columna] = filled_column
    return dataframe

def rellena_consecutivos(sin_aislados, columna):
    sin_nans = sin_aislados[columna].copy()
    df_interpolated = sin_nans.interpolate(method='spline')
    return sin_nans

def completa_nans(dataframe, columna):
    sin_aislados = rellena_aislados(dataframe, columna)
    if sin_aislados[columna].isnull().any():
        print("Hay nulos consecutivos")
        sin_nans = rellena_consecutivos(sin_aislados, columna)
    else:
        sin_nans = sin_aislados
    return sin_nans

if __name__ == "__main__":
    main_file_path = os.path.abspath(__file__)
    datos = cargador(os.path.join(os.path.dirname(main_file_path), "datos", "vic_elec_nans.csv"))

    serie = SerieTemporal(datos, "Time", "Demand")
    serie.dataframe = serie.dataframe.drop(columns=['Unnamed: 0', "Date"])
    serie.dataframe[serie.columna_valores] = completa_nans(serie.dataframe, serie.columna_valores)
    serie.dataframe["Temperature"] = completa_nans(serie.dataframe, "Temperature")
    serie.dataframe["Holiday"] = completa_nans(serie.dataframe, "Holiday")
    print(serie.dataframe.head(7))
    serie.descripcion()
    #serie.grafico_auto(120)
