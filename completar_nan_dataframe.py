import pandas as pd
from carga_datos import cargador

def completa_nan (dataframe):
# DataFrame de ejemplo
    completa = pd.DataFrame({'A': [1, 2, None, 4],
                   'B': [5, None, 7, None]})

# Reemplazar los NaN con la media de la columna
dataframe.rolling(3, center=True).mean().head()
print(completa_nan(dataframe))

if __name__ == "__main__":
    