import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA

# Obtén los datos de tu base de datos y guárdalos en un DataFrame de pandas llamado "df"

# Visualizar las series de tiempo
df.plot(subplots=True, figsize=(10, 6))
plt.show()

# Descomponer las series de tiempo en tendencia, estacionalidad y residuos
for col in df.columns:
    print(f"Descomposición para {col}:")
    result = seasonal_decompose(df[col], model='aditivo', period=30)
    result.plot()
    plt.show()

# Analizar las autocorrelaciones y autocorrelaciones parciales
for col in df.columns:
    print(f"ACF y PACF para {col}:")
    lag_acf = acf(df[col], nlags=20)
    lag_pacf = pacf(df[col], nlags=20)

    plt.subplot(121)
    plt.stem(lag_acf)
    plt.title('Función de Autocorrelación')

    plt.subplot(122)
    plt.stem(lag_pacf)
    plt.title('Función de Autocorrelación Parcial')
    plt.show()

# Aplicar un modelo ARIMA para predecir las series de tiempo
for col in df.columns:
    print(f"Modelo ARIMA para {col}:")
    modelo = ARIMA(df[col], order=(1, 0, 0))
    resultado = modelo.fit()
    print(resultado.summary())

    plt.plot(df[col])
    plt.plot(resultado.fittedvalues, color='red')
    plt.title(f"Modelo ARIMA para {col}")
    plt.show()
