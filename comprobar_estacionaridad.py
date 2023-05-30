import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

def comprobar_estacionaridad(columna_valor):
    # Realizar la prueba de Dickey-Fuller aumentada
    result_df = adfuller(columna_valor)
    Estadística_de_prueba_Dickey_Fuller = result_df[0]
    Valor_p1 = result_df[1]

    # Realizar la prueba de KPSS
    result_kpss = kpss(columna_valor)
    Estadística_de_prueba_KPSS = result_kpss[0]
    Valor_p2 = result_kpss[1]

    # Crear un diccionario con los valores
    data = {
        'Estadística_de_prueba': [Estadística_de_prueba_Dickey_Fuller, Estadística_de_prueba_KPSS],
        'Valor_p': [Valor_p1, Valor_p2]
    }

    # Crear el DataFrame
    df = pd.DataFrame(data)
    df = df.rename(index={0: 'Dickey Fuller', 1: 'KPSS'}, inplace=True)
    print(df)
    if Valor_p1 <= 0.05:
        print("Existe estacionaridad")
    elif Valor_p2 <= 0.05:
        print("No existe estacionaridad")
    return df

