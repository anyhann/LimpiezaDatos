import pandas as pd
from carga_datos import cargador

dataframe = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, None]})

def completa_nan(dataframe):
    # DataFrame de ejemplo
    # Reemplazar los NaN con la media de la columna
    dataframe.rolling(3, center=True).mean().head()



if __name__ == "__main__":
    print(completa_nan(dataframe))
    