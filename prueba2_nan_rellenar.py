import pandas as pd
import numpy as np

def completar_valores_nulos(dataframe, columna):
    '''
    Esta función rellena los valores nulos de la columna deseada con los métodos de interpolación, moda o media.
    '''
    metodo = input("Seleccione el método para completar los valores nulos:\n1. Interpolar.\n2. Moda. \n3. Media. \nIngrese el número correspondiente al método ---> ")

    if metodo == "1":
        dataframe[columna].interpolate(method = "linear", inplace = True)
    elif metodo == "2":
        moda = dataframe[columna].mode()[0]
        dataframe[columna].fillna(moda, inplace = True)
    elif metodo == "3":
        media = dataframe[columna].mean()
        dataframe[columna].fillna(media, inplace = True)
    else:
        print("Método inválido. No se realizaron cambios.")

    return dataframe

# Crear un DataFrame de ejemplo
data = {'A': [1, np.nan, 3, np.nan, np.nan, 6, 7],
        'B': [np.nan, 2, np.nan, 4, np.nan, 6, np.nan]}
df = pd.DataFrame(data)

# Rellenar los valores NaN en la columna 'A' utilizando interpolate
df_rellenado = completar_valores_nulos(df, 'A')

print(df_rellenado)