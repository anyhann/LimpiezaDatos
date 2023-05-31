import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
from matplotlib import pyplot as plt
from carga_serie_temporal import auto_conversion_datetime
from descripciones import descripcion

class SerieTemporal:
    def __init__(self, dataframe, columna_temporal, columna_valores):
        self.dataframe = self.conversion_a_serie_temp(dataframe, columna_temporal)
        self.columna_valores = columna_valores
        #self.conversion_a_serie_temp(dataframe, columna_temporal)

    def conversion_a_serie_temp(self, dataframe, columna):
        # Convertir la columna de texto a datetime
        dataframe[columna] = auto_conversion_datetime(dataframe[columna])
        dataframe.set_index(columna, inplace=True)
        dataframe = dataframe.asfreq(dataframe.index[1]-dataframe.index[0])
        print("La frecuencia de la serie temporal es:", dataframe.index.freq)
        dataframe = dataframe.sort_index()
        print(f'Número de filas con missing values: {dataframe.isnull().any(axis=1).sum()}')
        return dataframe

    def descripcion(self):
        print(descripcion(self.dataframe))
        print("La frecuencia de la serie temporal es:", self.dataframe.index.freq)
        print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')


    def grafico_auto (self, num_lags):
        fig, ax = plt.subplots(figsize=(7, 3))
        plot_acf(self.dataframe[self.columna_valores], ax=ax, lags=num_lags)
        plt.show()
    
    def verifica_nan(self):
        rango_completo = pd.date_range(
        start = self.dataframe.index.min(),
        end = self.dataframe.index.max(),
        freq = self.dataframe.index.freq)
        
        verificacion = (self.dataframe.index == rango_completo).all()
        if verificacion == True:
            print("No hay valores nulos")
        else:
            print("Hay valores nulos")
            print(f'Número de filas con missing values: {self.dataframe.isnull().any(axis=1).sum()}')
        return verificacion
    
    def __getattr__(self, attr):
        # Redirigir el acceso a los atributos al atributo 'dataframe'
        return getattr(self.dataframe, attr)
