import pandas as pd
from carga_datos import cargador
import os

def descripcion(datos :pd.DataFrame) -> pd.DataFrame:
  """
  Descripción estadística de los datos
  """
  salida = datos.describe(include = "all").T
  salida["Nulos"] = datos.isnull().sum()
  salida["Tipos"] = datos.dtypes
  return salida

if __name__ == "__main__":
  main_file_path = os.path.abspath(__file__)
  datos = cargador(os.path.join(os.path.dirname(main_file_path), "hormigon.csv"))
  print(descripcion(datos))