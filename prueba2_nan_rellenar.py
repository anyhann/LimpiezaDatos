import pandas as pd
import numpy as np
from LimpiezaDatos.utilidades.captura_opciones import leer_opciones_pantalla

def completar_valores_nulos(self, columna):
    '''
    Esta función rellena los valores nulos de la columna deseada con los métodos de interpolación, moda o media.
    '''
    dataframe = self.dataframe
    print("Seleccione el método para completar los valores nulos:")
    metodo = leer_opciones_pantalla({"1": "Interpolación lineal", "2": "Interpolación temporal", "3": "Moda", "4": "Media"})
    if metodo == "1":
        dataframe[columna].interpolate(method = "linear", inplace = True, limit_direction = "both")
    elif metodo == "2":
        dataframe[columna].interpolate(method = "time", inplace = True, limit_direction = "both")
    elif metodo == "3":
        moda = dataframe[columna].mode()[0]
        dataframe[columna].fillna(moda, inplace = True)
    elif metodo == "4":
        media = dataframe[columna].mean()
        dataframe[columna].fillna(media, inplace = True)
    else:
        print("Método inválido. No se realizaron cambios.")
    self.dataframe = dataframe
    return dataframe

# Crear un DataFrame de ejemplo
data = {'A': [1, np.nan, 3, np.nan, np.nan, 6, 7, 1, np.nan, np.nan],
        'B': [np.nan, 2, np.nan, 4, np.nan, 6, np.nan, 5, np.nan, np.nan]}
df = pd.DataFrame(data)

# Rellenar los valores NaN en la columna 'A' utilizando interpolate
df_rellenado = completar_valores_nulos(df, 'B')

print(df_rellenado)