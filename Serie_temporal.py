import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib as plt
from sklearn.preprocessing import StandardScaler
from carga_datos import cargador
from carga_serie_temporal import convertir_a_datetime


class SerieTemporal:
    def __init__(self, dataframe, columna_temporal, columna_valores):
        self.dataframe = self.conversion_a_serie_temp(dataframe, columna_temporal)

    def conversion_a_serie_temp(self, dataframe, columna):
        # Convertir la columna de texto a datetime
        dataframe[columna] = convertir_a_datetime(dataframe[columna])

        dataframe.set_index(columna, inplace=True)
        return dataframe


    def grafico_auto (self, columna_valor, num_lags):
        fig, ax = plt.subplots(figsize=(7, 3))
        plot_acf(columna_valor, ax=ax, lags=num_lags)
        plt.show()
    
