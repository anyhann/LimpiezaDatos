import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib as plt
from carga_datos import cargador

def grafico_autocorrelacion (columna_objetivo, num_lags):
    fig, ax = plt.subplots(figsize=(7, 3))
    plot_acf(columna_objetivo, ax=ax, lags=num_lags)
    plt.show()


class SerieTemporal:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def transformar_a_serie_temporal(self, columna_fecha, columna_valor):
        # Asegurarse de que la columna de fecha sea del tipo datetime
        self.dataframe[columna_fecha] = pd.to_datetime(self.dataframe[columna_fecha])

        # Establecer la columna de fecha como el índice del DataFrame
        self.dataframe.set_index(columna_fecha, inplace=True)

        # Ordenar el DataFrame por la columna de fecha en orden ascendente
        self.dataframe.sort_index(inplace=True)

        # Crear una serie temporal a partir de la columna de valores
        serie_temporal = pd.Series(self.dataframe[columna_valor])

        return serie_temporal
    def grafico_autocorrelacion (columna_valor, num_lags):
        fig, ax = plt.subplots(figsize=(7, 3))
        plot_acf(columna_valor, ax=ax, lags=num_lags)
        plt.show()