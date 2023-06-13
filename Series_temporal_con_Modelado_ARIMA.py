import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA

# Visualizar las series de tiempo en graficos separados
def visualizar_serie(dataframe):
    dataframe.plot(subplots=True, figsize=(10, 6))
    plt.show()

# Descomponer las series de tiempo en tendencia, estacionalidad y residuos
def seasonal_decompose_func(dataframe, num_period):
    modelo = int(input("Qué tipo de modelo quieres aplicar? (1/multiplicative, 2/additive): "))
    if modelo == 1:
        model = 'multiplicative'
    elif modelo == 2:
        model = 'additive'
    else:
        print("Opción no válida. Se utilizará el modelo 'additive' por defecto.")
        model = 'additive'
    
    result = seasonal_decompose(dataframe, model=model, period=num_period)
    
    trend = result.trend
    seasonal = result.seasonal
    residual = result.resid
    
    plt.figure(figsize=(10, 8))

    # Componente de tendencia
    plt.subplot(3, 1, 1)
    plt.plot(trend)
    plt.title('Componente de Tendencia')

    # Componente estacional
    plt.subplot(3, 1, 2)
    plt.plot(seasonal)
    plt.title('Componente Estacional')

    # Componente de residuos
    plt.subplot(3, 1, 3)
    plt.plot(residual)
    plt.title('Componente de Residuos')

    plt.tight_layout()
    plt.show()

    

# Analizar las autocorrelaciones y autocorrelaciones parciales
def autocor_graficos(dataframe, columna, num_lags):
    for columna in dataframe.columns:
        print(f"ACF y PACF para {columna}:")
        lag_acf = acf(dataframe[columna], nlags=num_lags)
        lag_pacf = pacf(dataframe[columna], nlags=num_lags)

        plt.subplot(121)
        plt.stem(lag_acf)
        plt.title('Función de Autocorrelación')

        plt.subplot(122)
        plt.stem(lag_pacf)
        plt.title('Función de Autocorrelación Parcial')
        plt.show()



# Separación datos train-val-test
def separacion_datos (dataframe, fin_train, fin_validacion):
    dataframe_train = dataframe.loc[: fin_train, :]
    dataframe_val   = dataframe.loc[fin_train:fin_validacion, :]
    dataframe_test  = dataframe.loc[fin_validacion:, :]
    
    print(f"Fechas train      : {dataframe_train.index.min()} --- {dataframe_train.index.max()}  (n={len(dataframe_train)})")
    print(f"Fechas validacion : {dataframe_val.index.min()} --- {dataframe_val.index.max()}  (n={len(dataframe_val)})")
    print(f"Fechas test       : {dataframe_test.index.min()} --- {dataframe_test.index.max()}  (n={len(dataframe_test)})")


def modelo(dataframe, order_pdq):
    for columna in dataframe.columns:
        print(f"Modelo ARIMA para {columna}:")
        p = int(input("¿Cuál es el valor de p?: "))
        d = int(input("¿Cuál es el valor de d?: "))
        q = int(input("¿Cuál es el valor de q?: "))
        order_pdq = [p, d, q]

        modelo = ARIMA(dataframe[columna], order=order_pdq)
        resultado = modelo.fit()
        print(resultado.summary())

        # Gráfico de los datos originales y los valores ajustados
        plt.plot(dataframe[columna])
        plt.plot(resultado.fittedvalues, color='red')
        plt.title(f"Modelo ARIMA para {columna}")
        plt.show()
