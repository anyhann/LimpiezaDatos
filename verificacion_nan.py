import pandas as pd


def verifica_nan(dataframe):
# Construimos un rango completo de tiempo desde el mínimo al máximo y con saltos iguales a la frecuencia...
rango_completo = pd.date_range(
    start=dataframe.index.min(),
    end=dataframe.index.max(),
    freq=dataframe.index.freq)

# ...y comprobamos que la columna índice (Time) coincide en todos los puntos
(dataframe.index == rango_completo).all()